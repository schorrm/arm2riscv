#!/usr/bin/python3

"""
Classes:
LDRB LoadRegisterByte
UMADDL UnsignedMultiplyAddLong
BL BranchAndLink
ADRP AddressPCRelative
ADD Add
MOV Move
STP StorePair
LDP LoadPair
RET Return
STR StoreRegister
LDR LoadRegister
MUL Multiply
"""

# Master Arm64Instruction Class, all others inherit from here
class Arm64Instruction:
    def __init__(self, operands):
        self.required_temp_regs = []
        self.specific_regs = []
        self.riscv_instructions = []

    def emit_riscv(self):
        pass
    
class LoadRegisterByte(Arm64Instruction):
    opcodes = ['ldrb']

    def __init__(self, operands):
        super().__init__(operands)
        dest = operands[0]
        src  = operands[1].register
        if 'offset' in operands[1].keys():
            offset = operands[1].offset
            self.riscv_instructions = [
                'lb {dest} , {offset}({src})'
            ]
            if writeback:
                self.riscv_instructions.append([
                    'add {src}, {offset}'
                ])
        else:
            self.riscv_instructions = [
                'lb {dest}, ({src})'
            ]        
    
class UnsignedMultiplyAddLong(Arm64Instruction):
    opcodes = ['umaddl']

    def __init__(self, operands):
        super().__init__(operands)
        regs = [x['register'] for x in operands[:4]]
        xd, wm, wn, xa = regs
        self.required_temp_regs = ['temp']
        self.specific_regs = [xd, wm, wn, xa]

    def emit_riscv(self):
        temp = self.required_temp_regs[0]
        xd, wm, wn, xa = self.specific_regs
        self.riscv_instructions = [
            f'mulw {temp}, {wm}, {wn}',
            f'add {xd}, {xa}, {temp}'
        ]
        
        
class BranchAndLink(Arm64Instruction):
    opcodes = ['bl']

    def __init__(self, operands):
        super().__init__(operands)
        label = operands[0]['label']
        self.riscv_instructions = [
            f'call {label}'
        ]

class Add(Arm64Instruction):
    opcodes = ['add']

    def __init__(self, operands):
        super().__init__(operands)
        dest, s1, s2 = operands
        self.op = 'ADDW' if dest['half_width'] else 'ADD'
        self.specific_regs = [dest['register'], s1['register']]
        if 'register' not in s2.keys():
            if 'label' in s2.keys():
                self.s2 = s2['label']
            elif 'immediate' in s2.keys():
                self.s2 = s2['immediate']
        else:
            self.s2 = False
            self.specific_regs.append(s2['register'])

    def emit_riscv(self):
        dest, s1, *xsource = self.specific_regs
        if xsource:
            self.s2 = xsource[0]
        self.riscv_instructions = [
            f'{self.op} {dest}, {s1}, {self.s2}'
        ]


class AddressPCRelative(Arm64Instruction):
    opcodes = ['adrp']

    def __init__(self, operands):
        super().__init__(operands)
        dest = operands[0]['register']
        self.specific_regs = [dest]
        self.label = operands[1]['label']

    def emit_riscv(self):
        dest = self.specific_regs[0]
        self.riscv_instructions = [
            f'lui {dest}, %hi({self.label})'
        ]

class Move(Arm64Instruction):
    opcodes = ['mov']

    def __init__(self, operands):
        super().__init__(operands)
        dest = operands[0]['register']
        src  = operands[1]
        self.specific_regs = [dest]
        if 'register' in src.keys():
            self.specific_regs.append(src['register'])
            self.source = False
        elif 'immediate' in src.keys():
            self.source = src['immediate']
        elif 'label' in src.keys():
            self.source = src['label']

    def emit_riscv(self):
        if len(self.specific_regs) > 1:
            self.source = self.specific_regs[1]
        
        self.dest = self.specific_regs[0]
        self.riscv_instructions = [
            f'add {self.dest}, x0, {self.source}'
        ]

class StorePair(Arm64Instruction):
    opcodes = ['stp']

    def __init__(self, operands):
        super().__init__(operands)

        r1, r2, sp = operands[:3]

        # Becomes either SW or SD, depending on reg width
        self.base_op = 'SW' if r1['half_width'] else 'SD'
        
        self.offset = 0
        if 'offset' in sp.keys():
            self.offset = sp['offset']
        if len(operands) == 4:
            post_index = True
            self.final_offset = operands[3]['immediate']
        elif sp['writeback']:
            pre_index  = True
            self.final_offset = sp['offset']
        else: # Signed Offset
            self.final_offset = None

        self.specific_regs = [r1['register'], r2['register'], sp['register']]

    def emit_riscv(self):
        r1, r2, sp = self.specific_regs
        self.riscv_instructions = [
            f'{self.base_op} {r1}, {self.offset}({sp})',
            f'{self.base_op} {r2}, {self.offset + 8}({sp})'
        ]

        if self.final_offset:
            self.riscv_instructions.append(
                f'addi {sp}, {sp}, {self.final_offset}'
            )
        

class LoadPair(Arm64Instruction):
    opcodes = ['ldp']

    def __init__(self, operands):
        super().__init__(operands)

        r1, r2, sp = operands[:3]

        # Becomes either LW or LD, depending on reg width
        self.base_op = 'LW' if r1['half_width'] else 'LD'
        
        self.offset = 0
        if 'offset' in sp.keys():
            self.offset = sp['offset']
        if len(operands) == 4:
            post_index = True
            self.final_offset = operands[3]['immediate']
        elif sp['writeback']:
            pre_index  = True
            self.final_offset = sp['offset']
        else: # Signed Offset
            self.final_offset = None

        self.specific_regs = [r1['register'], r2['register'], sp['register']]

    def emit_riscv(self):
        r1, r2, sp = self.specific_regs
        self.riscv_instructions = [
            f'{self.base_op} {r1}, {self.offset}({sp})',
            f'{self.base_op} {r2}, {self.offset + 8}({sp})'
        ]

        if self.final_offset:
            self.riscv_instructions.append(
                f'addi {sp}, {sp}, {self.final_offset}'
            )

class Return(Arm64Instruction):
    opcodes = ['ret']

    def __init__(self, operands):
        super().__init__(operands)
        self.riscv_instructions = ['ret']


# TODO: This class is a lot like Anthony Weiner. There are disasters
# wait to happen with sexts. Sign extension / overflow could be iffy
class Multiply(Arm64Instruction):
    opcodes = ['mul']

    # TODO: check type safety!
    def __init__(self, operands):
        super().__init__(operands)
        regs = [x['register'] for x in operands[:3]]
        xd, xa, xb = regs
        self.specific_regs = [xd, xa, xb]

    def emit_riscv(self):
        xd, xa, xb = self.specific_regs
        self.riscv_instructions = [
            f'mulw {xd}, {xa}, {xb}'
        ]


class StoreRegister(Arm64Instruction):
    opcodes = ['str']

    def __init__(self, operands):
        super().__init__(operands)

        r1, sp = operands[:2]

        # Becomes either SW or SD, depending on reg width
        self.base_op = 'SW' if r1['half_width'] else 'SD'
        
        self.offset = 0
        if 'offset' in sp.keys():
            self.offset = sp['offset']
        if len(operands) == 3:
            post_index = True
            self.final_offset = operands[3]['immediate']
        elif sp['writeback']:
            pre_index  = True
            self.final_offset = sp['offset']
        else: # Signed Offset
            self.final_offset = None

        self.specific_regs = [r1['register'],  sp['register']]

    def emit_riscv(self):
        r1, sp = self.specific_regs
        self.riscv_instructions = [
            f'{self.base_op} {r1}, {self.offset}({sp})',
        ]

        if self.final_offset:
            self.riscv_instructions.append(
                f'addi {sp}, {sp}, {self.final_offset}'
            )

class LoadRegister(Arm64Instruction):
    opcodes = ['ldr']

    def __init__(self, operands):
        super().__init__(operands)

        r1, sp = operands[:2]

        # Becomes either SW or SD, depending on reg width
        self.base_op = 'LW' if r1['half_width'] else 'LD'
        
        self.offset = 0
        if 'offset' in sp.keys():
            self.offset = sp['offset']
        if len(operands) == 3:
            post_index = True
            self.final_offset = operands[3]['immediate']
        elif sp['writeback']:
            pre_index  = True
            self.final_offset = sp['offset']
        else: # Signed Offset
            self.final_offset = None

        self.specific_regs = [r1['register'],  sp['register']]

    def emit_riscv(self):
        r1, sp = self.specific_regs
        self.riscv_instructions = [
            f'{self.base_op} {r1}, {self.offset}({sp})',
        ]

        if self.final_offset:
            self.riscv_instructions.append(
                f'addi {sp}, {sp}, {self.final_offset}'
            )


class Subtract(Arm64Instruction):
    # may get subs too
    opcodes = ['sub']

    def __init__(self, operands):
        super().__init__(operands)
        dest, s1, s2 = operands
        self.op = 'subw' if dest['half_width'] else 'sub'
        self.specific_regs = [dest['register'], s1['register']]
        if 'register' not in s2.keys():
            self.immediate = True 
            if 'label' in s2.keys():
                self.s2 = s2['label']
                # TODO: FIX
                # undefined behavior for now
            elif 'immediate' in s2.keys():
                self.s2 = s2['immediate']
            self.s2 = -self.s2 # invert the sign! now an add
            self.op = 'addiw' if dest['half_width'] else 'addi'
        else:
            self.immediate = False
            self.specific_regs.append(s2['register'])

    def emit_riscv(self):
        dest, s1, *xsource = self.specific_regs
        if not self.immediate:
            self.s2 = xsource[0]
        self.riscv_instructions = [
            f'{self.op} {dest}, {s1}, {self.s2}'
        ]

class Branch(Arm64Instruction):
    opcodes = ['b']
    # add conditionals to here? or separately?

    def __init__(self, operands):
        super().__init__(operands)
        target = operands[0]['label']
        self.riscv_instructions = [
            f'j {target}'
        ]

class LogicalShiftLeft(Arm64Instruction):
    opcodes = ['lsl']
    # May need to be fed into by implied shifts in OP2, tbd

    def __init__(self, operands):
        super().__init__(operands)

        dest, r1, r2 = operands
        wflag = 'W' if dest['half_width'] else ''
        dest = dest['register']
        dest = r1['register']
        self.specific_regs = [dest, r1]
        if 'register' in r2.keys():
            r2 = r2['register']
            self.specific_regs.append(r2)
            self.immediate = False
        else:
            self.immediate_op = r2['immediate']
            self.immediate = True
        
        self.op = 'slli' if self.immediate else 'sll'
        self.op += wflag
    
    def emit_riscv(self):
        dest, s1, *xsource = self.specific_regs
        if not self.immediate:
            self.s2 = xsource[0]
        else:
            self.s2 = self.immediate_op
        self.riscv_instructions = [
            f'{self.op} {dest}, {s1}, {self.s2}'
        ]
