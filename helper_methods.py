#!/usr/bin/python3

from register_map import register_map, mode_map
import copy

tempregs = ['s6', 's7', 's8']
membase_ptr = 's5'

def allocate_registers(registers, n_writes):
    current = 0
    loads = []
    stores = []
    for i in range(len(registers)):
        r = registers[i]
        mapped = register_map[r]
        if type(mapped) == int:
            offset = mapped
            loads.append(
                f'ld {tempregs[current]}, {offset}({membase_ptr})'
            )
            if i < n_writes:
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