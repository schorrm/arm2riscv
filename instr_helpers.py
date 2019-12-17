#!/usr/bin/python3

def isreg(d):
    if type(d) == dict:
        return 'register' in d.keys()
    return False


def wfreg(r):
    if 'half_width' in r.keys():
        if r['half_width']:
            return 'w'
    return ''


def safe_pullregs(operands):
    rs = []
    for o in operands:
        if 'register' in o.keys():
            rs.append(o['register'])
    return rs


def pulltypes(operands):
    o_types = []
    for o in operands:
        if 'register' in o.keys():
            o_types.append('register')
        elif 'immediate' in o.keys():
            o_types.append('immediate')
        elif 'label' in o.keys():
            o_types.append('label')
        else:
            o_types.append(None)
    return o_types


fpfmtmap = {
    16: 'h',
    32: 's',
    64: 'd',
    128: 'q'
}

float_load_fmt_map = {
    32: 'w',
    64: 'd',
    128: 'q'
}


def get_fl_flag(reg):
    """Return the appropriate RISC-V char suffix for the width
    """
    if type(reg) == dict:
        if 'width' in reg.keys():
            return fpfmtmap[reg['width']]


def get_fl_ld_flag(reg):
    if type(reg) == dict:
        if 'width' in reg.keys():
            return float_load_fmt_map[reg['width']]