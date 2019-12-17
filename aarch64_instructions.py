#!/usr/bin/python3

from typing import List

COMPARE = 'compare'  # name of register target for comparef
SHIFT_TEMP = 'shift_temp'
OP2_OVERSIZE = 'shift_temp'  # OP2 Imm / Shift should be mutually exclusive?

# little helper functions


def isreg(d):
    if type(d) == dict:
        return 'register' in d.keys()
    return False


def isOversizeOffset(o):
    if type(o) == int:
        return o >= 2048 or o < -2048
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

# Return the appropriate RISC-V char suffix for the width


def floatfmt(reg):
    return fpfmtmap[reg['width']]


def get_fl_flag(reg):
    if type(reg) == dict:
        if 'width' in reg.keys():
            return floatfmt(reg)


class Arm64Instruction:
    imm_width = 12
    num_reg_writes = 1

    # MAYBE: TODO: set lower bound to be 2 pow - 1 e.g. -2047 lower bound, to avoid edge case in subtract immediate? -- done for now
    def is_oversized_imm(self, x) -> bool:
        if 'immediate' in x.keys():
            x = x['immediate']
            if not self.imm_width:
                return True
            elif x not in range(- (2 ** (self.imm_width-1) + 1), 2 ** (self.imm_width-1)):
                return True
        return False

    def is_safe_imm(self, x) -> bool:
        if 'immediate' in x.keys():
            return not self.is_oversized_imm(x)
        return False

    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.operands = operands
        self.required_temp_regs = []
        self.specific_regs = safe_pullregs(operands)
        self.operand_types = pulltypes(operands)
        # used for checking which virtualized registers to write
        self.written_regs = self.specific_regs[:self.num_reg_writes]
        self.riscv_instructions = []
        self.immediate_value = None
        self.needs_synthesis = []

        if not operands:  # safeguard against nops, rets and other stuff like that
            return

        # WATCH THIS
        for operand in operands:
            if self.is_oversized_imm(operand):
                self.needs_synthesis.append(operand['immediate'])
                self.required_temp_regs.append(OP2_OVERSIZE)

        self.iflag = 'i' if any(self.is_safe_imm(o) for o in operands) else ''
        self.fp_wflag = get_fl_flag(operands[0])
        self.wflag = wfreg(operands[0])

    def get_args(self) -> List:
        """Get the arguments for the emit, with shift, immediate, and immediate temps interleaved

        Returns:
            List: List of arguments in format ready for output
        """
        rs = []
        reg_ct = 0
        for op, optype in zip(self.operands, self.operand_types):
            if optype == 'register':
                rs.append(self.specific_regs[reg_ct])
                reg_ct += 1
            elif optype == 'label':
                rs.append(op['label'])
            elif optype == 'immediate':
                if self.is_oversized_imm(op):
                    rs.append(self.required_temp_regs[0])
                else:
                    rs.append(op['immediate'])
        return rs

    def synthesize(self):
        for immediate, reg in zip(self.needs_synthesis, self.required_temp_regs):
            self.riscv_instructions.append(
                f'li {reg}, {immediate}'
            )

    def emit_riscv(self):
        self.synthesize()


def pullregs(operands):
    return [r['register'] for r in operands]


# converting umaddl: one arm instruction into two riscv instructions using one temp register
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
    """Convert sign extension, checking new constructor
    """
    opcodes = ['sxtw']

    def emit_riscv(self):
        xd, wn = self.specific_regs
        self.riscv_instructions = [
            f'sext.w {xd}, {wn}'
        ]

# converting bl: one arm instruction into one riscv instruction


class BranchAndLink(Arm64Instruction):
    opcodes = ['bl']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        label = operands[0]['label']
        self.riscv_instructions = [
            f'call {label}'
        ]


class Add(Arm64Instruction):
    """Converts Add

    Adjusts for immediate and width
    """
    opcodes = ['add']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.op = 'add' + self.iflag + self.wflag

    def emit_riscv(self):
        super().emit_riscv()
        dest, s1, s2 = self.get_args()
        self.riscv_instructions += [
            f'{self.op} {dest}, {s1}, {s2}'
        ]

# converting adrp: one arm instruction into one riscv instruction


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
    """Rewritten Move -- using simplified constructor

    Operation is li, la, or mv depending on argument type
    """
    opcodes = ['mov']
    imm_width = 64

    def emit_riscv(self):
        if self.operand_types[1] == 'immediate':
            op = 'li'
        elif self.operand_types[1] == 'label':
            op = 'la'
        else:
            op = 'mv'
        dest, src = self.get_args()
        self.riscv_instructions = [
            f'{op} {dest}, {src}'
        ]

# converting stp: one arm instruction into two or three riscv instructions
# three store instruction when sp changes, otherwise two


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
            pre_index = True
            self.final_offset = sp['offset']
        else:  # Signed Offset
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


# converting ldp: one arm instruction into two or three riscv instructions
# three load instruction when sp changes, otherwise two
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
            pre_index = True
            self.final_offset = sp['offset']
        else:  # Signed Offset
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
    """Convert Return - trivial conversion
    """
    opcodes = ['ret']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.riscv_instructions = ['ret']


class MultiplyDivide (Arm64Instruction):
    """Combining multiply and divide since should be the same

    converting mul, udiv or sdiv: simple 1:1
    TODO: This class is a lot like Anthony Weiner: There are disasters waiting
    to happen with sexts. Sign extension / overflow could be very iffy.
    """
    opcodes = ['mul', 'udiv', 'sdiv']

    map_op = {
        'mul': 'mul',
        'udiv': 'divu',
        'sdiv': 'div',
    }

    # TODO: check type safety!
    def emit_riscv(self):
        op = self.map_op[self.opcode]
        xd, xa, xb = self.specific_regs
        self.riscv_instructions = [
            f'{op}{self.wflag} {xd}, {xa}, {xb}'
        ]


class Negate(Arm64Instruction):
    """ Converts negate

    TODO: Do we need a word level op?
    """
    opcodes = ['neg']

    def emit_riscv(self):
        dest, source = self.specific_regs
        self.riscv_instructions = [
            f'sub {dest}, x0, {source}'
        ]


class Subtract(Arm64Instruction):
    """Handle Subtract

    Along with updating flags if it's `subs`
    If possible, switches a sub with immediate to addi with flipped sign.
    """
    opcodes = ['sub', 'subs']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.op = 'sub'
        if self.is_safe_imm(self.operands[2]):
            self.op = 'addi'
            self.immediate_value = -self.operands[2]['immediate']
        self.op += self.wflag
        if self.opcode == 'subs':
            self.specific_regs.append(COMPARE)

    def emit_riscv(self):
        super().emit_riscv()
        dest, s1, s2 = self.get_args()
        if self.immediate_value:
            s2 = self.immediate_value

        self.riscv_instructions += [
            f'{self.op} {dest}, {s1}, {s2}'
        ]

        if self.opcode == 'subs':
            cond = self.specific_regs[-1]
            self.riscv_instructions.append(
                f'mv {cond}, {dest} # update flags'
            )
            

class Branch(Arm64Instruction):
    """ Branch is jump, nothing else to it """
    opcodes = ['b']
    # add conditionals to here? or separately?

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        target = operands[0]['label']
        self.riscv_instructions = [
            f'j {target}'
        ]

class Shift(Arm64Instruction):
    """ convert shifts to corresponding name in RISC-V
    """
    
    opcodes = ['lsl', 'lsr', 'asr']
    # May need to be fed into by implied shifts in OP2, tbd

    opmap = {
        'lsl' : 'sll',
        'lsr' : 'srl',
        'asr' : 'sra',
    }

    def emit_riscv(self):
        dest, s1, s2 = self.get_args()
        self.riscv_instructions = [
            f'{self.opmap[self.opcode]}{self.iflag}{self.wflag} {dest}, {s1}, {s2}'
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

# converting ldr, ldrp, ldrsw or ldrsh: one arm instruction
# into one, two, three or four riscv instructions
# using temp for some of them


class LoadRegister(Arm64Instruction):
    opcodes = ['ldr', 'ldrb', 'ldrsw', 'ldrsh']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        r1, sp = operands[:2]

        if opcode == 'ldrb':
            self.base_op = 'lb'
        elif opcode == 'ldrsh':
            self.base_op = 'lh'
        elif r1['type'] == 'fp':
            store_suffix = 'w' if r1['width'] == 32 else floatfmt(r1)
            self.base_op = 'fl' + store_suffix
            self.float_st = True
        elif r1['half_width'] or opcode == 'ldrsw':
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
            pre_index = True
            self.final_offset = sp['offset']
        else:  # Signed Offset
            self.final_offset = None

        if isreg(self.offset):
            self.required_temp_regs = ['temp']
            self.reg_offset = self.offset['register']
            self.specific_regs.append(self.reg_offset)

        elif isOversizeOffset(self.offset):  # Max size for offset?
            self.required_temp_regs = ['temp']

        if self.final_offset:
            if isOversizeOffset(self.final_offset):
                self.required_temp_regs = ['temp']

        # TODO: check the specifics of relocation well
        elif sp.get('original_mode'):
            if 'got' in sp['original_mode']:  # GOT -- relocation
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
                    f'mv {sp}, {temp}'
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
                    f'mv {sp}, {temp}'
                )


"""
RISC-V stores
SB rs2,offset(rs1)	Store Byte	u8[rs1 + offset] ← rs2
SH rs2,offset(rs1)	Store Half	u16[rs1 + offset] ← rs2
SW rs2,offset(rs1)	Store Word	u32[rs1 + offset] ← rs2
SD rs2,offset(rs1)	Store Double	u64[rs1 + offset] ← rs2
"""

# converting str, strh, or strb: one arm instruction into two, three or four riscv instructions
# using temp register for some of them, depends on the offset


class StoreRegister(Arm64Instruction):
    opcodes = ['str', 'strh', 'strb']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        r1, sp = operands[:2]

        self.float_st = False
        if opcode == 'strb':
            self.base_op = 'sb'
        elif opcode == 'strh':
            self.base_op = 'sh'
        elif r1['type'] == 'fp':
            store_suffix = 'w' if r1['width'] == 32 else floatfmt(r1)
            self.base_op = 'fs' + store_suffix
            self.float_st = True
        elif r1['half_width']:
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
            pre_index = True
            self.final_offset = sp['offset']
        else:  # Signed Offset
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
                    f'mv {sp}, {temp}'
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
                    f'mv {sp}, {temp}'
                )


# Placeholder Compare -- may be swapped out later for fusion
# converting cmp: one arm instruction into one riscv instruction
# result is saved in the compare register
class Compare(Arm64Instruction):
    # may get subs too
    opcodes = ['cmp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        left, right = operands
        left = left['register']

        self.specific_regs = [COMPARE, left]

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

# converting ble, blt, bge, bgt, beq or bne: one arm instruction into one riscv instruction
# using the result of the last compare from the compare register


class ConditionalBranch(Arm64Instruction):
    opcodes = ['ble', 'blt', 'bge', 'bgt', 'beq', 'bne']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.target = operands[0]['label']
        self.specific_regs = [COMPARE]

    def emit_riscv(self):
        cmpreg = self.specific_regs[0]
        self.riscv_instructions = [
            f'{self.opcode} {cmpreg}, x0, {self.target}'
        ]

# Conditional operations
# Note: pray that '999999' is not being used as a numeric label elsewhere.
# We only go forward so multiple csels won't matter


class ConditionalSelect(Arm64Instruction):
    opcodes = ['csel']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.cc = operands[3]['label'].lower()
        self.specific_regs = [r['register'] for r in operands[:3]] + [COMPARE]
        # this allows cutting out a branch and simplifying
        self.required_temp_regs = ['temp']
        self.wf = wfreg(operands[0])

    def emit_riscv(self):
        dest, s1, s2, cond = self.specific_regs
        temp = self.required_temp_regs[0]
        self.riscv_instructions = [
            f'add{self.wf} {temp}, {s1}, x0',
            f'b{self.cc} {cond}, x0, 999999f',
            f'add{self.wf} {temp}, {s2}, x0',
            f'999999:',
            f'add{self.wf} {dest}, x0, {temp}'
        ]


# converting exclusive-or: one arm instruction into one riscv instruction
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

# converting Or: one arm instruction into one riscv instruction


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

# converting nop: one arm instruction into one riscv instruction


class Nop(Arm64Instruction):
    opcodes = ['nop']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.riscv_instructions = ['nop']


# Floating Point Instructions
# Use this for all simple 1:1 conversions
class FloatingPointSimplex(Arm64Instruction):
    opcodes = ['fadd', 'fsub', 'fdiv', 'fmul', 'fmax', 'fmin']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.specific_regs = pullregs(operands)
        self.width = floatfmt(operands[0])
        self.op = opcode

    def emit_riscv(self):
        dst, s1, s2 = self.specific_regs
        self.riscv_instructions = [
            f'{self.op}.{self.width} {dst}, {s1}, {s2}'
        ]


class FloatingPointSingleArg(Arm64Instruction):
    opcodes = ['fneg', 'fsqrt']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.specific_regs = pullregs(operands)
        self.width = floatfmt(operands[0])
        self.op = opcode

    def emit_riscv(self):
        dst, s1 = self.specific_regs
        self.riscv_instructions = [
            f'{self.op}.{self.width} {dst}, {s1}'
        ]


class FloatingPointFused(Arm64Instruction):
    opcodes = ['fmadd', 'fmsub', 'fnmadd', 'fnmsub']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.specific_regs = pullregs(operands)
        self.width = floatfmt(operands[0])
        self.op = opcode

    def emit_riscv(self):
        dst, s1, s2, s3 = self.specific_regs
        self.riscv_instructions = [
            f'{self.op}.{self.width} {dst}, {s1}, {s2}, {s3}'
        ]
