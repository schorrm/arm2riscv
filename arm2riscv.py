#!/usr/bin/python3

# The initial component: convert a file to a dict representation of the machine code

from lark import Lark, Transformer
from convert_parse_tree import TreeToDict
from register_map import register_map, mode_map
import sys
from utils import *
import copy
from tqdm import tqdm

from aarch64_instructions import Arm64Instruction

tempregs = ['s6', 's7', 's8']
membase_ptr = 's5'
def allocate_registers(registers):
    current = 0
    loads = []
    stores = []
    # TODO: replace with more efficient version with pointers
    for i in range(len(registers)):
        r = registers[i]
        mapped = register_map[r]
        if type(mapped) == int:
            offset = mapped
            loads.append(
                f'ld {tempregs[current]}, {offset}({membase_ptr})'
            )
            stores.append(
                f'sd {tempregs[current]}, {offset}({membase_ptr})'
            )
            registers[i] = tempregs[current]
            current += 1
        else:
            registers[i] = mapped
    return loads, stores    

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

def get_shifts(operand): # use after cleanup
    if 'shift' in operand.keys():
        shift = copy.deepcopy(operand['shift'])
        operand = operand['shift']['shift_reg']
        operand['register'] = 'shift_temp'
        return shift

    elif 'offset' in operand.keys():
        if type(operand['offset']) == dict:
            if 'shift' in operand['offset'].keys():
                shift = copy.deepcopy(operand['offset']['shift'])
                operand['offset'] = operand['offset']['shift']['shift_reg']
                operand['offset']['register'] = 'shift_temp'
                return shift
    
    return None

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
        shifts = None
        for operand in operands:
            shifts = get_shifts(operand)
            if shifts:
                tmpreg = {
                    'register': 'shift_temp',
                    'half_width' : shifts['shift_reg']['half_width']
                }
                op = shifts['shift_type']
                # TODO: remove the shift_by if it is RRX
                buffer.append(
                    instructions[op](op, [tmpreg, shifts['shift_reg'], shifts['shift_by']])
                )
        buffer.append(instructions[opcode](opcode, operands))
    else:
        buffer.append(line)
        if 'label' in d.keys():
            if d['label'] == 'main:':
                buffer.append('\tla s5, REG_BANK')

# Remove arch directive
if buffer[0].strip().startswith('.arch'):
    buffer.pop(0)

buffer.insert(1, reg_labels)
memguards_loads  = []
memguards_stores = []
 
# second pass: convert registers
for i, line in enumerate(buffer):
    if Arm64Instruction in type(line).__mro__:
        line.required_temp_regs = [register_map[r] for r in line.required_temp_regs]
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
            print(f'\t{ld}')
        line.emit_riscv()
        for l in line.riscv_instructions:
            print(f'\t{l}') 
        for st in stores:
            print(f'\t{st}')
    else:
        print(line.strip())
