plain_register_map = {
 'x0': 'x10',
 'w0': 'x10',
 'x1': 'x11',
 'w1': 'x11',
 'x2': 'x12',
 'w2': 'x12',
 'x3': 'x13',
 'w3': 'x13',
 'x4': 'x14',
 'w4': 'x14',
 'x5': 'x15',
 'w5': 'x15',
 'x6': 'x16',
 'w6': 'x16',
 'x7': 'x17',
 'w7': 'x17',
 'x8': 'x9',
 'w8': 'x9',
 'x9': 'x5',
 'w9': 'x5',
 'x10': 'x6',
 'w10': 'x6',
 'x11': 'x7',
 'w11': 'x7',
 'x12': 'x28',
 'w12': 'x28',
 'x13': 'x29',
 'w13': 'x29',
 'x14': 'x30',
 'w14': 'x30',
 'x15': 'x31',
 'w15': 'x31',
 'x19': 'x18',
 'w19': 'x18',
 'x20': 'x19',
 'w20': 'x19',
 'x21': 'x20',
 'w21': 'x20',
 'x22': 'x21',
 'w22': 'x21',
 'x23': 'x22',
 'w23': 'x22',
 'x24': 'x23',
 'w24': 'x23',
 'x25': 'x24',
 'w25': 'x24',
 'x26': 'x25',
 'w26': 'x25',
 'x27': 'x26',
 'w27': 'x26',
 'x28': 'x27',
 'w28': 'x27',
 'x29': 'x8',
 'w29': 'x8',
 'x30': 'x1',
 'w30': 'x1',
 'x31': 'x2',
 'w31': 'x2',
 'fp': 'fp',
 'sp': 'sp',
 'pc': 'pc',
 'wzr': 'x0',
 'xzr': 'x0',
 'lr': 'ra',
 'temp': 'x9',
 'x16': 'x9',
 'compare' : 'x9'
 }

abi_register_map = {
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
 'temp': 't4',
 'shift_temp': 't4',
 'x14': 't5',
 'compare' : 't5',
 'x15': 't6',
 'x16': 't6',
 'x17': '',
 'x18': '',
 'x19': 's2',
 'x20': 's3',
 'x21': 's4',
 'x22': 's5',
 'x23': 's6',
 'x24': 's7',
 'x25': 's8',
 'x26': 's9',
 'x27': 's10',
 'x28': 's11',
 'x29': 's0',
 'x30': 'ra',
 'xzr': 'x0',
 'sp': 'sp',
 'pc': 'pc'}


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
 'compare' : 's9',
 'banked_temp_1' : 's6',
 'banked_temp_2' : 's7',
 'banked_temp_3' : 's8',
 'bank_pointer'  : 's5',
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
 'pc': 'pc'}

mode_map = {
    'lo12' : 'lo',
    'got'  : 'hi', # not sure about risc-v relocs
    'got_lo12' : 'lo', # not sure about risc-v relocs
}

register_map = {}
for k, v in new_abi_register_map.items():
    register_map[k] = v
    if k.startswith('x'):
        register_map['w'+k[1:]] = v


for i in range(32):
    register_map[f'h{i}'] = f'f{i + 10 % 32}'
    register_map[f's{i}'] = f'f{i + 10 % 32}'
    register_map[f'd{i}'] = f'f{i + 10 % 32}'