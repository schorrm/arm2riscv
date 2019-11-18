#!/usr/bin/python3


from lark import Lark, Transformer

class TreeToDict(Transformer):
    def register(self, r):
        (r,) = r
        return r
    def offset(self, n):
        (n,) = n
        if 'immediate' in n.keys():
            n = n['immediate']
        return {'offset': n}
    def hex_val(self, v):
        (v,) = v
        return int(v, 16)
    def immediate(self, d):
        (d,) = d
        return {'immediate' : int(d)}
    def opcode(self, o):
        (o,) = o
        return {'opcode': str(o)}
    def indirect(self, l):
        d = {k: v for d in l for k, v in d.items()}
        d['indirect'] = True
        return d
    def writeback(self, w):
        return True
    def operand(self, op):
        wb = len(op) > 1
        op = op[0]
        return {'operand': op, 'writeback': wb}
    def operation(self, c):
        return {'operation' : {
            'opcode': c[0]['opcode'],
            'operands': c[1:]
        }}
    def start(self,d):
        if not d:
            return d
        (d,) = d
        return d
    def directive(self,d):
        (d,) = d
        return {'directive': str(d)}
    def label_target(self, l):
        (l,) = l
        return {'label': str(l)}
    def mode(self, m):
        (m,) = m
        return str(m)
    def proc_load(self, l):
        mode, label = l
        return {'proc_load': {
            'mode' : mode,
            'label' : label
        }}
    def label(self, l):
        (l,) = l
        return {'label': l}

    def half_reg(self, r):
        (r,) = r
        return {
            'register': str(r),
            'half_width': True
        }
    def full_reg(self, r):
        (r,) = r
        return {
            'register': str(r),
            'half_width': False
        }

    
    def shifted_register(self, r):
        reg, stype, *by = r
        if by:
            by = by[0]
            if type(by) != dict:
                by = int(by)
        else:
            by = None
        return {'shift':  {
            'shift_reg' : reg,
            'shift_type': stype,
            'shift_by'  : by
        } }
    def shift_by(self, o):
        (o,) = o
        return o
    def shift_type(self, t):
        (t,) = t
        return str(t)