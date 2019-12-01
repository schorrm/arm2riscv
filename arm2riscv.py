#!/usr/bin/python3

# The initial component: convert a file to a dict representation of the machine code

from lark import Lark, Transformer
from convert_parse_tree import TreeToDict
from register_map import register_map, mode_map
import sys
from utils import *
from helper_methods import *

import copy
from tqdm import tqdm

from aarch64_instructions import Arm64Instruction

import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-annot", "--annot-source", help="show original lines as comments",
                        action="store_true")
arg_parser.add_argument('-l', '--log-special', help="""log various changes (const synthesis,
                        register usage for emulating features, etc.)
                        (not yet available)""",
                        action="store_true")
args = arg_parser.parse_args()

instructions = {}
for ins in Arm64Instruction.__subclasses__():
    for opcode in ins.opcodes:
        instructions[opcode] = ins

transformer = TreeToDict()

with open('grammar/grammar_arm.lark') as f:
    grammar = f.read()

l = Lark(grammar, parser='earley')

buffer = []

ops = set()

COMCHAR = '#' # define comment character

# first pass: setup buffer with objects
for line in sys.stdin:
    tree = l.parse(line)
    d = transformer.transform(tree)
    if not d:  # for empty from comments / weird directives
        continue
    if 'operation' in d.keys():
        if args.annot_source:
            buffer.append(f'\t{COMCHAR} {line.strip()}') # add original line as comment
        opcode = d['operation']['opcode']
        if opcode not in instructions.keys():
            raise InstructionNotRecognized(opcode)  # for now ends program
            buffer.append(line + 'XXXXX')
            continue

        operands = [cleanup(operand) for operand in d['operation']['operands']]
        shifts = None
        for operand in operands:
            shifts = get_shifts(operand)
            if shifts:
                tmpreg = {
                    'register': 'shift_temp',
                    'half_width': shifts['shift_reg']['half_width']
                }
                op = shifts['shift_type']
                # TODO: remove the shift_by if it is RRX
                buffer.append(
                    instructions[op](
                        op, [tmpreg, shifts['shift_reg'], shifts['shift_by']])
                )
        buffer.append(instructions[opcode](opcode, operands))
    else:
        buffer.append(line)
        if 'label' in d.keys():
            if d['label'] == 'main:':
                # inject pointer to register bank on memory
                buffer.append('\tla\ts5, REG_BANK')

# Remove arch directive
if buffer[0].strip().startswith('.arch'):
    buffer.pop(0)

buffer.insert(1, reg_labels)
memguards_loads = []
memguards_stores = []

# second pass: convert registers
for i, line in enumerate(buffer):
    if Arm64Instruction in type(line).__mro__:
        line.required_temp_regs = [register_map[r]
                                   for r in line.required_temp_regs]
        loads, stores = allocate_registers(line.specific_regs)
        memguards_loads.append(loads)
        memguards_stores.append(stores)
    else:
        memguards_loads.append([])
        memguards_stores.append([])

# third pass: emit
for loads, stores, line in zip(memguards_loads, memguards_stores, buffer):
    if Arm64Instruction in type(line).__mro__:
        for ld in loads:
            ld = ld.replace(' ','\t',1) # replace first space with tab for cleaner formatting
            print(f'\t{ld}')
        line.emit_riscv()
        for l in line.riscv_instructions:
            fl = l.replace(' ','\t',1) # replace first space with tab for cleaner formatting
            print(f'\t{fl}')
        for st in stores:
            st = st.replace(' ','\t',1) # replace first space with tab for cleaner formatting
            print(f'\t{st}')
    else:
        print(line.rstrip())
