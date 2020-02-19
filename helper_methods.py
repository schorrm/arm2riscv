#!/usr/bin/python3

from register_map import register_map, mode_map, base_register_map
import copy

tempregs = ['s6', 's7', 's8']
membase_ptr = 's5'

base_tempregs = ['x22', 'x23', 'x24']
base_membase_ptr = 'x21'

# TODO: add example here
def allocate_registers(registers, n_writes, use_base=False):
    ''' issue loads and stores for operations on memory mapped registers
    '''

    _rmap = base_register_map if use_base else register_map
    _tregs = base_tempregs if use_base else tempregs
    _membase_ptr = base_membase_ptr if use_base else membase_ptr
    current = 0
    loads = []
    stores = []
    for i in range(len(registers)):
        r = registers[i]
        mapped = _rmap[r]
        if type(mapped) == int: # mapper gives the offset instead of a string name for mmapped registers
            offset = mapped
            loads.append(
                f'ld {_tregs[current]}, {offset}({_membase_ptr})' # RISC-V load of mmapped
            )
            if i < n_writes:
                stores.append(
                    f'sd {_tregs[current]}, {offset}({_membase_ptr})' # RISC-V store mmapped
                )
            registers[i] = _tregs[current]
            current += 1
        else:
            registers[i] = mapped
    return loads, stores  


# TODO: Move to transformer
# Note before / after
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