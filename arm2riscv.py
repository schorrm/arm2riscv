#!/usr/bin/python3

# The initial component: convert a file to a dict representation of the machine code

from lark import Lark, Transformer
from convert_parse_tree import TreeToDict
from register_map import register_map, mode_map, base_register_map
import sys
from utils import *
from helper_methods import *

import copy
from tqdm import tqdm
import csv

from aarch64_instructions import Arm64Instruction

import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-annot", "--annot-source", help="show original lines as comments",
                        action="store_true")
arg_parser.add_argument("-p", "--permissive", help="allow untranslated operations",
                        action="store_true")
arg_parser.add_argument("-xnames", "--xnames", help="Use xnames instead of ABI names",
                        action="store_true")
arg_parser.add_argument('-logfile', '--logfile', help='Log table of used instructions to file')
arg_parser.add_argument('-vi', '--view-instructions', help="List opcodes with defined conversions and exit",
                        action="store_true")
args = arg_parser.parse_args()

if args.logfile and not args.annot_source:
    print('ERROR: Logging cannot be used without annotation enabled!')
    exit(1)

# Build map of opcodes to their handling instruction subclasses
instructions = {}
for ins in Arm64Instruction.__subclasses__():
    for opcode in ins.opcodes:
        instructions[opcode] = ins

if args.view_instructions:
    for i, opcode in enumerate(sorted(instructions.keys()), 1):
        print(f'{i}.\t{opcode}')
    exit(0)

transformer = TreeToDict()

with open('grammar/grammar_arm.lark') as f:
    grammar = f.read()

l = Lark(grammar, parser='earley')

buffer = []

ops = set()

COMCHAR = '#'  # define comment character

# first pass: setup buffer with objects
for line in sys.stdin:
    tree = l.parse(line)
    d = transformer.transform(tree)
    if not d:  # for empty from comments / weird directives
        continue
    if 'operation' in d.keys():
        if args.annot_source:
            # add original line as comment
            buffer.append(f'\t{COMCHAR} {line.strip()}')
        opcode = d['operation']['opcode']
        if opcode not in instructions.keys():
            if not args.permissive:
                raise InstructionNotRecognized(opcode)  # end program if in restrictive mode
            else:
                buffer.append(line.rstrip() + '\t!!!!!')  # print the line with a warning sequence
                continue

        operands = [cleanup(operand) for operand in d['operation']['operands']]
        shifts = None
        for operand in operands:
            # Find shifted registers and pull them out and
            # promote to shift_reg temp register
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
                mbptr = 's5' if not args.xnames else 'x21'
                buffer.append(f'\tla\t{mbptr}, REG_BANK')

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
        loads, stores = allocate_registers(line.specific_regs, line.num_reg_writes, args.xnames)
        memguards_loads.append(loads)
        memguards_stores.append(stores)
    else:
        memguards_loads.append([])
        memguards_stores.append([])


# third pass: emit
for loads, stores, line in zip(memguards_loads, memguards_stores, buffer):
    if Arm64Instruction in type(line).__mro__:
        for ld in loads:
            # replace first space with tab for cleaner formatting
            ld = ld.replace(' ', '\t', 1)
            print(f'\t{ld} # load of mmapped register')
        line.emit_riscv()
        for l in line.riscv_instructions:
            # replace first space with tab for cleaner formatting
            fl = l.replace(' ', '\t', 1)
            print(f'\t{fl}')
        for st in stores:
            # replace first space with tab for cleaner formatting
            st = st.replace(' ', '\t', 1)
            print(f'\t{st} # store of mmapped register')

    else:
        if line.strip().startswith('.xword'):  # = dword, but not recognized on RV
            line = line.replace('.xword', '.dword', 1)
        print(line.rstrip())

# NEW: Adding option to put out table of all instruction conversions
# THIS MUST BE USED WITH ANNOT, we have a check for that at the top
if not args.logfile:
    exit(0)

log_buffer = []
# We will do this as an extra pass
for loads, stores, line in zip(memguards_loads, memguards_stores, buffer):
    if Arm64Instruction in type(line).__mro__:
        translation = ''
        for ld in loads:
            # replace first space with tab for cleaner formatting
            ld = ld.replace(' ', '\t', 1)
            translation += f'{ld} # load of mmapped register\n'
        # line.emit_riscv()
        for l in line.riscv_instructions:
            # replace first space with tab for cleaner formatting
            fl = l.replace(' ', '\t', 1)
            translation += f'{fl}\n'
        for st in stores:
            # replace first space with tab for cleaner formatting
            st = st.replace(' ', '\t', 1)
            translation += f'{st} # store of mmapped register\n'
        prev_line = prev_line.replace('#', '').strip()
        prev_inst = prev_line.split()[0]
        log_buffer.append(
            [prev_inst, prev_line.replace('#', '').strip(), translation.strip()]
        )
    elif line.strip().startswith('#'):
        prev_line = line

with open(args.logfile, 'a') as f:
    wtr = csv.writer(f)
    wtr.writerows(log_buffer)
