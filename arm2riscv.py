#!/usr/bin/python3

# The initial component: convert a file to a dict representation of the machine code

from lark import Lark, Transformer
from convert_parse_tree import TreeToDict
from register_map import abi_register_map, mode_map
import sys
from utils import *

register_map = {}
for k, v in abi_register_map.items():
    register_map[k] = v
    if k.startswith('x'):
        register_map['w'+k[1:]] = v

from aarch64_instructions import Arm64Instruction

def cleanup(operand):
    operand['operand']['writeback'] = operand['writeback']
    operand = operand['operand']
    if 'proc_load' in operand.keys():
        operand['original_mode'] = operand['proc_load']['mode']
        mode = mode_map[operand['proc_load']['mode']]
        label = operand['proc_load']['label']['label']
        operand['label'] = f'%{mode}({label})'
        operand['is_load'] = True
    elif 'offset' in operand.keys():
        if type(operand['offset']) == dict:
            if 'proc_load' in operand['offset'].keys():
                operand['original_mode'] = operand['offset']['proc_load']['mode']
                mode = mode_map[operand['offset']['proc_load']['mode']]
                label = operand['offset']['proc_load']['label']['label']
                operand['offset'] = f'%{mode}({label})'
            
    return operand

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

# first pass: setup buffer with objects
for line in sys.stdin:
    tree = l.parse(line)
    d = transformer.transform(tree)
    if 'operation' in d.keys():
        opcode = d['operation']['opcode']
        if opcode not in instructions.keys():
            raise InstructionNotRecognized(opcode)
            buffer.append(line + 'XXXXX')
            continue

        operands = [cleanup(operand) for operand in d['operation']['operands']]
        buffer.append(instructions[opcode](opcode, operands))
    else:
        buffer.append(line)

# Remove arch directive
if buffer[0].strip().startswith('.arch'):
    buffer.pop(0)

# second pass: convert registers
for line in buffer:
    if Arm64Instruction in type(line).__mro__:
        line.required_temp_regs = [register_map[r] for r in line.required_temp_regs]
        line.specific_regs = [register_map[r] for r in line.specific_regs]


# third pass: emit
for line in buffer:
    if Arm64Instruction in type(line).__mro__:
        line.emit_riscv()
        for l in line.riscv_instructions:
            print(f'\t{l}') 
    else:
        print(line.strip())
