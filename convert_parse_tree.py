#!/usr/bin/python3

from lark import Lark, Transformer

# Change: inline the GOT label conversions
from register_map import mode_map
import copy

class TreeToDict(Transformer):
    def register(self, r):
        (r,) = r
        return r

    def hex_val(self, v):
        (v,) = v
        return int(v, 16)

    def immediate(self, d):
        (d,) = d
        return {'immediate': int(d)}

    def opcode(self, o):
        (o,) = o
        o = o.replace('.','') # Remove dots in opcodes, e.g. b.eq
        return {'opcode': str(o)}

    def indirect(self, l):
        d = {k: v for d in l for k, v in d.items()}
        d['indirect'] = True
        return d

    def writeback(self, w):
        return True

    def operand(self, op):
        wb = len(op) > 1  # Only way to have more than one child item here is writeback
        op = op[0]
        op['writeback'] = wb
        return op
        # return {'operand': op, 'writeback': wb}

    def operation(self, c):
        return {'operation': {
            'opcode': c[0]['opcode'],
            'operands': c[1:]
        }}

    def start(self, d):
        if not d:
            return d
        (d,) = d
        return d

    def directive(self, d):
        (d,) = d
        return {'directive': str(d)}

    def label_target(self, l):
        (l,) = l
        return {'label': str(l)}

    def mode(self, m):
        (m,) = m
        return str(m)

    # Inlining conversion of preprocessor load
    def proc_load(self, l):
        mode, label = l
        label = label['label']

        new_mode = mode_map[mode]
        return {
            'original_mode': mode,
            'label': f'%{new_mode}({label})',
            'is_load': True
        }

    def offset(self, n):
        (n,) = n
        if 'immediate' in n.keys():
            n = n['immediate']
            return {'offset': n}
        mode = n.get('original_mode')
        if mode:
            return {
                'offset': n['label'],
                'original_mode': mode
            }
        return {'offset': n}

    def label(self, l):
        (l,) = l
        return {'label': l}

    def half_reg(self, r):
        (r,) = r
        return {
            'register': str(r),
            'type': 'gp',
            'half_width': True
        }

    def full_reg(self, r):
        (r,) = r
        return {
            'register': str(r),
            'type': 'gp',
            'half_width': False
        }

    def double64(self, r):
        (r,) = r
        return {
            'register': str(r),
            'width': 64
        }

    def float32(self, r):
        (r,) = r
        return {
            'register': str(r),
            'width': 32
        }

    def float16(self, r):
        (r,) = r
        return {
            'register': str(r),
            'width': 16
        }

    def float_reg(self, r):
        (r,) = r
        r['type'] = 'fp'
        return r

    # Can we clean this up?
    def shifted_register(self, r):
        reg, stype, *by = r
        if by:
            by = by[0]
            if type(by) != dict:
                by = int(by)
        else:
            by = None
        rdict = copy.deepcopy(reg)
        rdict['register'] = 'shift_temp'
        rdict['shift'] = {
            'shift_reg': reg,
            'shift_type': stype,
            'shift_by': by
        }
        return rdict

    def shift_by(self, o):
        (o,) = o
        return o

    def shift_type(self, t):
        (t,) = t
        return str(t)
