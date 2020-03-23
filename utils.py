#!/usr/bin/python3

class InstructionNotRecognized(Exception):
    ''' Exception to throw when an instruction does not have defined conversion code '''
    pass


reg_labels = """        .section .tdata
REG_BANK:
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
"""