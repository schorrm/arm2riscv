#!/usr/bin/python3

class InstructionNotRecognized(Exception):
    pass


reg_labels = """
.section .tdata
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