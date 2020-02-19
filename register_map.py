new_abi_register_map = {
    'x0': 'a0',
    'x1': 'a1',
    'x2': 'a2',
    'x3': 'a3',
    'x4': 'a4',
    'x5': 'a5',
    'x6': 'a6',
    'x7': 'a7',
    'x8': 's1',
    'x9': 't0',
    'x10': 't1',
    'x11': 't2',
    'x12': 't3',
    'x13': 't4',
    'x14': 't5',
    'x15': 't6',
    'x16': 's11',
    'temp': 's11',
    'shift_temp': 's10',
    'compare': 's9',
    'banked_temp_1': 's6',
    'banked_temp_2': 's7',
    'banked_temp_3': 's8',
    'bank_pointer': 's5',
    'x17': 0,
    'x18': 8,
    'x19': 's2',
    'x20': 's3',
    'x21': 's4',
    'x22': 16,
    'x23': 24,
    'x24': 32,
    'x25': 40,
    'x26': 48,
    'x27': 56,
    'x28': 64,
    'x29': 's0',
    'x30': 'ra',
    'xzr': 'x0',
    'sp': 'sp',
    'pc': 'pc'
}

abi_to_base = {
    'a0': 'x10',
    'a1': 'x11',
    'a2': 'x12',
    'a3': 'x13',
    'a4': 'x14',
    'a5': 'x15',
    'a6': 'x16',
    'a7': 'x17',
    't0': 'x5',
    't1': 'x6',
    't2': 'x7',
    't3': 'x28',
    't4': 'x29',
    't5': 'x30',
    't6': 'x31',
    'gp': 'x3',
    'tp': 'x4',
    's1': 'x9',
    's2': 'x18',
    's3': 'x19',
    's4': 'x20',
    's5': 'x21',
    's6': 'x22',
    's7': 'x23',
    's8': 'x24',
    's9': 'x25',
    's10': 'x26',
    's11': 'x27',
    's0': 'x8',
    'ra': 'x1',
    'sp': 'x2',
    'zero': 'x0',
    'pc': 'pc'
}

mode_map = {
    'lo12': 'lo',
    'got': 'hi',  # not sure about risc-v relocs
    'got_lo12': 'lo',  # not sure about risc-v relocs
}

register_map = {}
for k, v in new_abi_register_map.items():
    register_map[k] = v
    if k.startswith('x'):
        register_map['w'+k[1:]] = v

for i in range(32):
    register_map[f'h{i}'] = f'f{(i + 10) % 32}'
    register_map[f's{i}'] = f'f{(i + 10) % 32}'
    register_map[f'd{i}'] = f'f{(i + 10) % 32}'

# Base Register Map = not the ABI names 
base_register_map = register_map.copy()
for k, v in base_register_map.items():
    if v in abi_to_base.keys():
        base_register_map[k] = abi_to_base[v]

