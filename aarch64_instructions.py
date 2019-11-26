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

# little helper functions

def isreg(d):
    if type(d) == dict:
        return 'register' in d.keys()
    return False

def isOversizeOffset(o):
    if type(o) == int:
        return o >= 2048 or o < -2048
    return False

# Master Arm64Instruction Class, all others inherit from here
class Arm64Instruction:
    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.required_temp_regs = []
        self.specific_regs = []
        self.riscv_instructions = []

    def emit_riscv(self):
        pass
      
    
class UnsignedMultiplyAddLong(Arm64Instruction):
    opcodes = ['umaddl']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
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

class SignExtendWord(Arm64Instruction):
    opcodes = ['sxtw']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        xd, wn = operands
        self.specific_regs = [xd['register'], wn['register']]

    def emit_riscv(self):
        xd, wn = self.specific_regs
        self.riscv_instructions = [
            f'sext.w {xd}, {wn}'
        ]
        
        
class BranchAndLink(Arm64Instruction):
    opcodes = ['bl']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        label = operands[0]['label']
        self.riscv_instructions = [
            f'call {label}'
        ]

class Add(Arm64Instruction):
    opcodes = ['add']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        dest, s1, s2 = operands
        self.specific_regs = [dest['register'], s1['register']]
        if 'register' not in s2.keys():
            self.op = 'addi'
            if 'label' in s2.keys():
                self.s2 = s2['label']
            elif 'immediate' in s2.keys():
                self.s2 = s2['immediate']
                if isOversizeOffset(self.s2):
                    self.required_temp_regs = ['temp']
                    self.op = 'add'
        else:
            self.op = 'add'
            self.s2 = False
            self.specific_regs.append(s2['register'])
        if dest['half_width']:
            self.op += 'w'

    def emit_riscv(self):
        dest, s1, *xsource = self.specific_regs
        if xsource:
            self.s2 = xsource[0]
        if self.required_temp_regs:
            temp = self.required_temp_regs[0]
            self.riscv_instructions = [
                f'li {temp}, {self.s2}',
                f'add {dest}, {s1}, {temp}'
            ]
        else:
            self.riscv_instructions = [
                f'{self.op} {dest}, {s1}, {self.s2}'
            ]


class AddressPCRelative(Arm64Instruction):
    opcodes = ['adrp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        dest = operands[0]['register']
        self.specific_regs = [dest]
        self.label = operands[1]['label']
        if 'is_load' not in operands[1].keys():
            self.label = f'%hi({self.label})'

    def emit_riscv(self):
        dest = self.specific_regs[0]
        self.riscv_instructions = [
            f'lui {dest}, {self.label}'
        ]

class Move(Arm64Instruction):
    opcodes = ['mov']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        dest = operands[0]['register']
        src  = operands[1]
        self.specific_regs = [dest]
        self.stype = None
        if 'register' in src.keys():
            self.specific_regs.append(src['register'])
            self.source = False
        elif 'immediate' in src.keys():
            self.source = src['immediate']
            self.stype = 'immediate'
        elif 'label' in src.keys():
            self.source = src['label']
            self.stype = 'label'

    def emit_riscv(self):
        if len(self.specific_regs) > 1:
            self.source = self.specific_regs[1]
        
        self.dest = self.specific_regs[0]
        if self.stype == 'immediate':
            self.riscv_instructions = [
                f'li {self.dest}, {self.source}'
            ]
        elif self.stype == 'label':
            self.riscv_instructions = [
                f'la {self.dest}, {self.source}'
            ]
        else:            
            self.riscv_instructions = [
                f'add {self.dest}, x0, {self.source}'
            ]


class StorePair(Arm64Instruction):
    opcodes = ['stp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        r1, r2, sp = operands[:3]

        # Becomes either sw or sd, depending on reg width
        self.base_op = 'sw' if r1['half_width'] else 'sd'
        
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

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        r1, r2, sp = operands[:3]

        # Becomes either lw or ld, depending on reg width
        self.base_op = 'lw' if r1['half_width'] else 'ld'
        
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

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.riscv_instructions = ['ret']


# TODO: This class is a lot like Anthony Weiner. There are disasters
# wait to happen with sexts. Sign extension / overflow could be iffy
# combining multiply and divide / rem since should be the same
class MultiplyDivide (Arm64Instruction):
    opcodes = ['mul', 'udiv', 'sdiv']

    map_op = {
        'mul': 'mul',
        'udiv': 'divu',
        'sdiv': 'div',
    }

    # TODO: check type safety!
    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        regs = [x['register'] for x in operands[:3]]
        wflag = 'w' if operands[0]['half_width'] else ''
        xd, xa, xb = regs
        self.specific_regs = [xd, xa, xb]
        self.op = self.map_op[opcode] + wflag

    def emit_riscv(self):
        xd, xa, xb = self.specific_regs
        self.riscv_instructions = [
            f'{self.op} {xd}, {xa}, {xb}'
        ]

class Subtract(Arm64Instruction):
    opcodes = ['sub', 'subs']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        dest, s1, s2 = operands
        self.opcode = opcode
        self.oversized = False
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
            if isOversizeOffset(self.s2):
                self.op = 'sub'
                self.oversized = True
                self.s2 = -self.s2
                self.required_temp_regs = ['temp']
            else:
                self.op = 'addiw' if dest['half_width'] else 'addi'
        else:
            self.immediate = False
            self.specific_regs.append(s2['register'])

        if self.opcodes == 'subs':
            self.specific_regs.append('compare')


    def emit_riscv(self):
        dest, s1, *xsource = self.specific_regs
        if not self.immediate:
            self.s2 = xsource[0]
        if self.oversized:
            temp = self.required_temp_regs[0]
            self.riscv_instructions = [
                f'li {temp}, {self.s2}',
                f'{self.op} {dest}, {s1}, {temp}'
            ]
        else:
            self.riscv_instructions = [
                f'{self.op} {dest}, {s1}, {self.s2}'
            ]
        
        if self.opcode == 'subs':
            if self.immediate:
                cond = xsource[0]
            else:
                cond = xsource[1]
            self.riscv_instructions.append(
                f'add {cond}, {dest}, x0'
            )

class Branch(Arm64Instruction):
    opcodes = ['b']
    # add conditionals to here? or separately?

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        target = operands[0]['label']
        self.riscv_instructions = [
            f'j {target}'
        ]

class Shift(Arm64Instruction):
    opcodes = ['lsl', 'lsr', 'asr']
    # May need to be fed into by implied shifts in OP2, tbd

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        if opcode == 'lsl':
            self.op = 'sll'
        elif opcode == 'lsr':
            self.op = 'srl'
        elif opcode == 'asr':
            self.op = 'sra'
        dest, r1, r2 = operands
        wflag = 'w' if dest['half_width'] else ''
        dest = dest['register']
        r1 = r1['register']
        self.specific_regs = [dest, r1]
        if 'register' in r2.keys():
            r2 = r2['register']
            self.specific_regs.append(r2)
            self.immediate = False
        else:
            self.immediate_op = r2['immediate']
            self.immediate = True
        
        if self.immediate:
            self.op += 'i'
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


"""
RISC-V Load Types
LB rd,offset(rs1)	Load Byte	rd ← s8[rs1 + offset]
LH rd,offset(rs1)	Load Half	rd ← s16[rs1 + offset]
LW rd,offset(rs1)	Load Word	rd ← s32[rs1 + offset]
LBU rd,offset(rs1)	Load Byte Unsigned	rd ← u8[rs1 + offset]
LHU rd,offset(rs1)	Load Half Unsigned	rd ← u16[rs1 + offset]
LWU rd,offset(rs1)	Load Word Unsigned	rd ← u32[rs1 + offset]
LD rd,offset(rs1)	Load Double	rd ← u64[rs1 + offset]
"""

class LoadRegister(Arm64Instruction):
    opcodes = ['ldr', 'ldrb', 'ldrsw', 'ldrsh']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        r1, sp = operands[:2]

        if opcode == 'ldrb':
            self.base_op = 'lb'
        elif opcode == 'ldrsh':
            self.base_op = 'lh'
        elif r1['half_width'] or opcode=='ldrsw':
            self.base_op = 'lw'
        else:
            self.base_op = 'ld'

        self.reg_offset = False

        # Becomes either SW or SD, depending on reg width
        self.specific_regs = [r1['register'],  sp['register']]
        
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

        if isreg(self.offset):
            self.required_temp_regs = ['temp']
            self.reg_offset = self.offset['register']
            self.specific_regs.append(self.reg_offset)
        
        elif isOversizeOffset(self.offset): # Max size for offset?
            self.required_temp_regs = ['temp']

        if self.final_offset:
            if isOversizeOffset(self.final_offset):
                self.required_temp_regs = ['temp']

        # TODO: check the specifics of relocation well
        elif sp.get('original_mode'):
            if 'got' in sp['original_mode']: # GOT -- relocation
                self.base_op = 'add'
        

    # TODO: Change this to use the destination register if D != SP
    # Note: this requires moving the offset commit to the line before the load, 
    # instead of the line after
    def emit_riscv(self):
        r1, sp, *self.reg_offset = self.specific_regs
        if self.reg_offset:
            self.reg_offset = self.reg_offset[0]
        if self.base_op == 'add':
            self.riscv_instructions = [
                f'{self.base_op} {r1}, {sp}, {self.offset}'
            ]
        elif self.required_temp_regs and not self.reg_offset:
            temp = self.required_temp_regs[0]
            self.riscv_instructions = [
                f'li {temp}, {self.offset}',
                f'add {temp}, {temp}, {sp}',
                f'{self.base_op} {r1}, ({temp})'
            ]
            if self.final_offset:
                self.riscv_instructions.append(
                    f'add {sp}, x0, {temp}'
                )
        elif not self.reg_offset:
            self.riscv_instructions = [
                f'{self.base_op} {r1}, {self.offset}({sp})',
            ]

            if self.final_offset:
                self.riscv_instructions.append(
                    f'addi {sp}, {sp}, {self.final_offset}'
                )
        
        else:
            temp = self.required_temp_regs[0]
            self.riscv_instructions = [
                f'add {temp}, {sp}, {self.reg_offset}',
                f'{self.base_op} {r1}, ({temp})'
            ]

            if self.final_offset:
                self.riscv_instructions.append(
                    f'add {sp}, x0, {temp}'
                )


"""
RISC-V stores
SB rs2,offset(rs1)	Store Byte	u8[rs1 + offset] ← rs2
SH rs2,offset(rs1)	Store Half	u16[rs1 + offset] ← rs2
SW rs2,offset(rs1)	Store Word	u32[rs1 + offset] ← rs2
SD rs2,offset(rs1)	Store Double	u64[rs1 + offset] ← rs2
"""

class StoreRegister(Arm64Instruction):
    opcodes = ['str', 'strh', 'strb']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        r1, sp = operands[:2]

        if opcode == 'strb':
            self.base_op = 'sb'
        elif opcode =='strh':
            self.base_op = 'sh'
        elif r1['half_width'] or opcode=='strsw':
            self.base_op = 'sw'
        else:
            self.base_op = 'sd'

        self.reg_offset = False

        # Becomes either SW or SD, depending on reg width
        
        self.offset = 0
        if 'offset' in sp.keys():
            self.offset = sp['offset']

        self.specific_regs = [r1['register'],  sp['register']]
        if len(operands) == 3:
            post_index = True
            self.final_offset = operands[3]['immediate']
        elif sp['writeback']:
            pre_index  = True
            self.final_offset = sp['offset']
        else: # Signed Offset
            self.final_offset = None

        if isreg(self.offset):
            self.required_temp_regs = ['temp']
            self.reg_offset = self.offset['register']
            self.specific_regs.append(self.reg_offset)
        
        elif isOversizeOffset(self.offset) or isOversizeOffset(self.final_offset):
            self.required_temp_regs = ['temp']


    def emit_riscv(self):
        r1, sp, *self.reg_offset = self.specific_regs
        if self.reg_offset:
            self.reg_offset = self.reg_offset[0]
        if self.required_temp_regs and not self.reg_offset:
            temp = self.required_temp_regs[0]
            self.riscv_instructions = [
                f'li {temp}, {self.offset}',
                f'add {temp}, {temp}, {sp}',
                f'{self.base_op} {r1}, ({temp})'
            ]
            if self.final_offset:
                self.riscv_instructions.append(
                    f'add {sp}, x0, {temp}'
                )

        elif not self.reg_offset:
            self.riscv_instructions = [
                f'{self.base_op} {r1}, {self.offset}({sp})',
            ]

            if self.final_offset:
                self.riscv_instructions.append(
                    f'addi {sp}, {sp}, {self.final_offset}'
                )
        
        elif self.reg_offset:
            temp = self.required_temp_regs[0]
            self.riscv_instructions = [
                f'add {temp}, {sp}, {self.reg_offset}',
                f'{self.base_op} {r1}, ({temp})'
            ]

            if self.final_offset:
                self.riscv_instructions.append(
                    f'add {sp}, x0, {temp}'
                )


# Placeholder Compare -- to be swapped out later for fusion

class Compare(Arm64Instruction):
    # may get subs too
    opcodes = ['cmp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        left, right = operands
        left = left['register']

        self.specific_regs = ['compare', left]

        self.immediate = not isreg(right)

        if isreg(right):
            right = right['register']
            self.specific_regs.append(right)
        else:
            right = right['immediate']
            self.immediate_arg = right


    def emit_riscv(self):
        op = 'sub'
        cmpreg, left, *right = self.specific_regs
        if self.immediate:
            right = -self.immediate_arg
            op = 'addi'
        else:
            right = right[0]
        self.riscv_instructions = [
            f'{op} {cmpreg}, {left}, {right}'
        ]

class ConditionalBranch(Arm64Instruction):
    opcodes = ['ble', 'blt', 'bge', 'bgt', 'beq', 'bne']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.target = operands[0]['label']
        self.specific_regs = ['compare']

    def emit_riscv(self):
        cmpreg = self.specific_regs[0]
        self.riscv_instructions = [
            f'{self.opcode} {cmpreg}, x0, {self.target}'
        ]

class ExclusiveOr(Arm64Instruction):
    opcodes = ['eor']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        dest, r1, op2 = operands
        self.specific_regs = [dest['register'], r1['register']]

        self.immediate = not isreg(op2)
        self.baseop = 'xor' if isreg(op2) else 'xori'
        if not self.immediate:
            self.specific_regs.append(op2['register'])
        else:
            self.immediate_arg = op2['immediate']

    def emit_riscv(self):
        dest, r1, *r2 = self.specific_regs
        if self.immediate:
            r2 = self.immediate_arg
        else:
            r2 = r2[0]
        self.riscv_instructions = [
            f'{self.baseop} {dest}, {r1}, {r2}'
        ]

class Or(Arm64Instruction):
    opcodes = ['orr']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        dest, r1, op2 = operands
        self.specific_regs = [dest['register'], r1['register']]

        self.immediate = not isreg(op2)
        self.baseop = 'or' if isreg(op2) else 'ori'
        if not self.immediate:
            self.specific_regs.append(op2['register'])
        else:
            self.immediate_arg = op2['immediate']

    def emit_riscv(self):
        dest, r1, *r2 = self.specific_regs
        if self.immediate:
            r2 = self.immediate_arg
        else:
            r2 = r2[0]
        self.riscv_instructions = [
            f'{self.baseop} {dest}, {r1}, {r2}'
        ]

class Nop(Arm64Instruction):
    opcodes = ['nop']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.riscv_instructions = ['nop']