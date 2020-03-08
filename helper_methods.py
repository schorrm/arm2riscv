#!/usr/bin/python3

from register_map import register_map, mode_map, base_register_map
import copy

tempregs = ['s6', 's7', 's8']
membase_ptr = 's5'

base_tempregs = ['x22', 'x23', 'x24']
base_membase_ptr = 'x21'


def allocate_registers(registers, n_writes, use_base=False):
    ''' issue loads and stores for operations on memory mapped registers
        Example of allocate:
            lsl   x10, x18, 5
        becomes:
            ld      s6, 8(s5) # load of mmapped register
            slli    t1, s6, 5
        Or, 
            mov   x18, x1
        becomes:
            ld      s6, 8(s5) # load of mmapped register
            mv      s6, a1
            sd      s6, 8(s5) # store of mmapped register
    '''

    _register_map = base_register_map if use_base else register_map
    _tempregs = base_tempregs if use_base else tempregs
    _membase_ptr = base_membase_ptr if use_base else membase_ptr
    current = 0
    loads = []
    stores = []
    for i in range(len(registers)):
        r = registers[i]
        mapped = _register_map[r]
        if type(mapped) == int:  # mapper gives the offset instead of a string name for mmapped registers
            offset = mapped
            loads.append(
                f'ld {_tempregs[current]}, {offset}({_membase_ptr})'  # RISC-V load of mmapped
            )
            if i < n_writes:
                stores.append(
                    f'sd {_tempregs[current]}, {offset}({_membase_ptr})'  # RISC-V store mmapped
                )
            registers[i] = _tempregs[current]
            current += 1
        else:
            registers[i] = mapped
    return loads, stores


# DONE: Move to transformer
# Note before / after
# NOTE: function was nerfed altogether!

# Modified: just get the shifts, no longer mutating the tree
def get_shifts(operand):
    if 'shift' in operand.keys():
        shift = operand['shift']
        return shift

    elif 'offset' in operand.keys():
        if type(operand['offset']) == dict:
            if 'shift' in operand['offset'].keys():
                shift = operand['offset']['shift']
                return shift
    return None
