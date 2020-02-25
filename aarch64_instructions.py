#!/usr/bin/python3

from typing import List
from instr_helpers import *

COMPARE = 'compare'  # name of register target for comparef
SHIFT_TEMP = 'shift_temp'
OP2_OVERSIZE = 'shift_temp'  # OP2 Imm / Shift should be mutually exclusive?
TEMP = 'temp'


class Arm64Instruction:
    imm_width = 12
    num_reg_writes = 1

    def is_oversized_imm(self, x) -> bool:
        if 'immediate' in x.keys():
            x = x['immediate']
            if not self.imm_width:
                return True
            elif x not in range(- (2 ** (self.imm_width-1) + 1), 2 ** (self.imm_width-1)):
                ''' Note: 2 ** (self.imm_width-1) + 1 is not tight, it is actually up to - 2** imm_width-1.
                However: this allows us to invert immediates where necessary for signed ops without incurring
                problems in edge cases.
                '''
                return True
        return False

    def is_oversized_int(self, x) -> bool:
        if type(x) != int:
            return False
        if x not in range(- (2 ** (self.imm_width-1) + 1), 2 ** (self.imm_width-1)):
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
        
        # Get our registers and types (these are recurring patterns)
        self.specific_regs = safe_pullregs(operands)
        self.operand_types = pulltypes(operands)
        # used for checking which virtualized registers to write
        self.written_regs = self.specific_regs[:self.num_reg_writes]
        self.riscv_instructions = []
        self.immediate_value = None
        self.needs_synthesis = []
        self.set_offset_reg = None
        self.offset = 0

        if not operands:  # safeguard against nops, rets and other stuff like that
            return

        # See if this can be made cleaner
        for operand in operands:
            if self.is_oversized_imm(operand):
                self.needs_synthesis.append(operand['immediate'])
                self.required_temp_regs.append(OP2_OVERSIZE)

            elif 'offset' in operand.keys():
                if self.is_oversized_int(operand['offset']):
                    self.needs_synthesis.append(operand['offset'])
                    self.required_temp_regs.append(OP2_OVERSIZE)
                    self.set_offset_reg = (
                        len(self.specific_regs), self.specific_regs.index(operand['register']))
                    self.specific_regs.append(OP2_OVERSIZE)
                elif type(operand['offset']) == int:
                    self.offset = operand['offset']
                elif isreg(operand['offset']):
                    self.set_offset_reg = (
                        len(self.specific_regs), self.specific_regs.index(operand['register']))
                    self.specific_regs.append(operand['offset']['register'])
                    self.required_temp_regs.append(OP2_OVERSIZE)

        self.iflag = 'i' if any(self.is_safe_imm(o) for o in operands) else ''
        self.fp_wflag = get_fl_flag(operands[0])
        self.wflag = is_half_width(operands[0])

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

    def emit_riscv(self):
        for immediate, reg in zip(self.needs_synthesis, self.required_temp_regs):
            self.riscv_instructions.append(
                f'li {reg}, {immediate} # synthesis of oversized immediate'
            )

        if self.set_offset_reg:
            x, y = self.set_offset_reg
            x = self.specific_regs[x]
            y = self.specific_regs[y]
            self.riscv_instructions.append(
                f'add {self.required_temp_regs[-1]}, {x}, {y} # converting offset register to add'
            )


class UnsignedMultiplyAddLong(Arm64Instruction):
    """converting umaddl: one arm instruction into two riscv instructions using one temp register
    """
    opcodes = ['umaddl']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.required_temp_regs = ['temp']

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


class BranchAndLink(Arm64Instruction):
    """BL is completely equivalent to a 'call'
    """
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

    def emit_riscv(self):
        super().emit_riscv()
        dest, s1, s2 = self.get_args()
        self.riscv_instructions += [
            f'add{self.iflag}{self.wflag} {dest}, {s1}, {s2}'
        ]


class AddressPCRelative(Arm64Instruction):
    """ADRP works like LUI in practice, at least w/ GCC
    """
    opcodes = ['adrp']
    imm_width = 20

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
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


class MoveNot(Arm64Instruction):
    ''' MVN - move not
    '''
    opcodes = ['mvn']
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
            f'{op} {dest}, {src}',
            f'not {dest}, {dest}'
        ]


class MoveWideWithKeep(Arm64Instruction):
    ''' MOVK --> A relatively complex sequence of operations
    Arm64 docs: 
    "Move wide with keep moves an optionally-shifted 16-bit immediate value into a register, keeping other bits unchanged."
    (https://developer.arm.com/docs/ddi0596/e/base-instructions-alphabetic-order/movk-move-wide-with-keep)
    There's no such primitive instruction in RISC-V, so we're gonna put it together here.
    Broadly, we'll:
    (1) Clear the bits we're going to load into in the destination (ANDing a mask)
    (2) Move the bits to the parallel area
    (3) or them together
    Yay Turing Machines!
    '''
    opcodes = ['movk']
    imm_width = 64  # we will handle our own immediates here

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.required_temp_regs = ['temp', 'shift_temp']
        self.shift = False
        if len(self.operands) > 2:  # Not just a movk, but shifted
            self.shift = True
            # Operands are e.g. movk    x0, 0x41df, lsl 48
            # We never need to pull the shift, since it can only be LSL
            self.shamt = self.operands[3]['immediate']

    def emit_riscv(self):
        temp, shift_temp = self.required_temp_regs
        dest = self.specific_regs[0]
        imm = self.operands[1]['immediate']
        self.riscv_instructions = [
            f'not {temp}, x0 # set reg to all ones',
            f"srli {temp}, {temp}, 48 # this clears the upper 48 bits in the mask. We'll invert it to get the final mask",
            f"li {shift_temp}, {imm} # load our immediate value"
        ]
        if self.shift:
            self.riscv_instructions += [
                f'slli {shift_temp}, {shift_temp}, {self.shamt} # move the immediate to the parallel place',
                f'slli {temp}, {temp}, {self.shamt} # move the mask to the parallel place'
            ]
        self.riscv_instructions += [
            f'not {temp}, {temp} # flip the mask to AND against',
            f'and {dest}, {dest}, {temp} # clear the target bits in mask',
            f'or {dest}, {dest}, {shift_temp} # or in the bits from the immediate to load'
        ]


class LoadStorePair(Arm64Instruction):
    """Load and Store pair have almost identical behavior.

    Most of the weird stuff is just accounting for writeback.
    """
    opcodes = ['ldp', 'stp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.num_reg_writes = 0 if opcode == 'stp' else 2

        # Becomes either lw or ld, depending on reg width
        addon = 'w' if self.wflag else 'd'
        self.base_op = self.opcode[0] + addon

        if len(operands) == 4:
            post_index = True
            self.final_offset = operands[3]['immediate']
        elif self.operands[2]['writeback']:
            pre_index = True
            self.final_offset = self.offset
        else:  # Signed Offset
            self.final_offset = None

    def emit_riscv(self):
        r1, r2, sp = self.specific_regs
        self.riscv_instructions = [
            f'{self.base_op} {r1}, {self.offset}({sp})',
            f'{self.base_op} {r2}, {self.offset + 8}({sp})'
        ]

        if self.final_offset:
            self.riscv_instructions.append(
                f'addi {sp}, {sp}, {self.final_offset} # writeback'
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
                f'mv {cond}, {dest} # simulating updating flags'
            )


class Branch(Arm64Instruction):
    """ Branch is jump, nothing else to it """
    opcodes = ['b']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        target = operands[0]['label']
        self.riscv_instructions = [
            f'j {target}'
        ]


class Shifts(Arm64Instruction):
    """ convert shifts to corresponding name in RISC-V
    """

    opcodes = ['lsl', 'lsr', 'asr']
    opmap = {
        'lsl': 'sll',
        'lsr': 'srl',
        'asr': 'sra',
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

RISC-V stores
SB rs2,offset(rs1)	Store Byte	u8[rs1 + offset] ← rs2
SH rs2,offset(rs1)	Store Half	u16[rs1 + offset] ← rs2
SW rs2,offset(rs1)	Store Word	u32[rs1 + offset] ← rs2
SD rs2,offset(rs1)	Store Double	u64[rs1 + offset] ← rs2
"""


class LoadStoreRegister(Arm64Instruction):
    """The behavior here is roughly equivalent for L/S.

    Load and Store are mixed together because the SP behavior (the complicated part here) is basically identical.
    """
    opcodes = ['ldr', 'ldrb', 'ldrsw', 'ldrsh', 'str', 'strh', 'strb']
    opmap = {
        'ldrb': 'lb',
        'ldrsh': 'lh',
        'ldrsw': 'lw',
        'ldr': 'ld',
        'str': 'sd',
        'strh': 'sh',
        'strb': 'sb'
    }

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        if self.opcode[0] == 's':
            self.num_reg_writes = 0

        r1, sp = operands[:2]

        self.base_op = self.opmap[self.opcode]

        if self.opcode not in ('ldr', 'str'):
            pass
        elif r1['type'] == 'fp':
            self.base_op = 'f' + self.opcode[0] + get_fl_flag(r1)
            self.float_st = True
        elif self.wflag:
            self.base_op = self.opcode[0] + 'w'

        self.reg_offset = False

        if len(operands) == 3:
            post_index = True
            self.final_offset = operands[2]['immediate']
        elif sp['writeback']:
            pre_index = True
            self.final_offset = self.offset
        else:  # Signed Offset
            self.final_offset = None

        # TODO: check the specifics of relocation well
        if sp.get('original_mode'):
            if 'got' in sp['original_mode']:  # GOT -- relocation
                self.base_op = 'add'
                self.offset = sp['offset']

    def emit_riscv(self):
        super().emit_riscv()
        dest, sp, *reg_offset = self.specific_regs
        if self.base_op == 'add':
            self.riscv_instructions.append(
                f'{self.base_op} {dest}, {sp}, {self.offset}'
            )
            return
        load_src = sp
        if self.set_offset_reg:
            load_src = self.required_temp_regs[0]
        self.riscv_instructions.append(
            f'{self.base_op} {dest}, {self.offset}({load_src})'
        )
        if self.final_offset:
            if self.required_temp_regs:
                self.riscv_instructions.append(
                    f'mv {sp}, {load_src} # writeback'
                )
            else:
                self.riscv_instructions.append(
                    f'addi {sp}, {sp}, {final_offset} # writeback'
                )


class Compare(Arm64Instruction):
    """Compare: sets the comparison arithmetically."""
    opcodes = ['cmp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.specific_regs.append(COMPARE)

    def emit_riscv(self):
        lhs, rhs = self.get_args()
        cmpreg = self.specific_regs[-1]
        op = 'sub'
        if self.is_safe_imm(self.operands[1]):
            rhs = -rhs
            op = 'addi'
        self.riscv_instructions = [
            f'{op} {cmpreg}, {lhs}, {rhs}'
        ]


class ConditionalBranch(Arm64Instruction):
    """Conditional branches are about the same, just check the last comparison to zero

    """
    opcodes = ['ble', 'blt', 'bge', 'bgt', 'beq', 'bne', 'bpl', 'bhi']

    opmap = dict(zip(opcodes, opcodes))
    opmap['bpl'] = 'bge'
    opmap['bhi'] = 'bgt'

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.target = operands[0]['label']
        self.specific_regs = [COMPARE]

        self.op = self.opmap[self.opcode]

    def emit_riscv(self):
        cmpreg = self.specific_regs[0]
        self.riscv_instructions = [
            f'{self.op} {cmpreg}, x0, {self.target}'
        ]


class ConditionalBranchNonZero(Arm64Instruction):
    ''' CBNZ -- branch if R!=0
    '''
    opcodes = ['cbnz']

    def emit_riscv(self):
        r = self.specific_regs[0]
        target = self.operands[1]['label']
        self.riscv_instructions = [
            f'bne {r}, x0, {target}'
        ]


class ConditionalSelect(Arm64Instruction):
    """Conditional Select uses a local branch to guard the condition
    Note: pray that '999999' is not being used as a numeric label elsewhere.
    We only go forward so multiple csels won't matter
    TODO: add checking for the numeric local in cleanup
    """
    opcodes = ['csel']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.cc = operands[3]['label'].lower()
        self.specific_regs.append(COMPARE)
        # this allows cutting out a branch and simplifying
        self.required_temp_regs = ['temp']

    def emit_riscv(self):
        dest, s1, s2, cond = self.specific_regs
        temp = self.required_temp_regs[0]
        self.riscv_instructions = [
            f'add{self.wflag} {temp}, {s1}, x0',
            f'b{self.cc} {cond}, x0, 999999f',  # f -- only forward.
            f'add{self.wflag} {temp}, {s2}, x0',
            f'999999:',
            f'add{self.wflag} {dest}, x0, {temp}'
        ]


class ConditionalSet(Arm64Instruction):
    """Conditional Set uses a local branch to guard the condition
    """
    opcodes = ['cset']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.cc = operands[1]['label'].lower()
        self.specific_regs.append(COMPARE)

    def emit_riscv(self):
        dest, cmp = self.specific_regs
        self.riscv_instructions = [
            f'li {dest}, 1',
            f'b{self.cc} {cmp}, x0, 999999f',  # f -- only forward.
            f'mv {dest}, x0',
            f'999999:',
            f'nop'  # nothing further needed, we just need to conditionally skip setting to 0
        ]


class BitwiseOperations(Arm64Instruction):
    """ Convert Bitwise operations (same pattern)
    """
    opcodes = ['eor', 'orr', 'and']
    opmap = {
        'eor': 'xor',
        'orr': 'or',
        'and': 'and',
    }

    def emit_riscv(self):
        dest, s1, s2 = self.get_args()
        self.riscv_instructions += [
            f'{self.opmap[self.opcode]}{self.iflag} {dest}, {s1}, {s2}'
        ]


class Nop(Arm64Instruction):
    """ This is pretty self-explanatory
    """
    opcodes = ['nop']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.riscv_instructions = ['nop']


# Floating Point Instructions

class FloatingPointMove(Arm64Instruction):
    opcodes = ['fmov']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        if self.fp_wflag:
            self.op = f'fmv.{self.fp_wflag}.x'
        else:
            self.op = f'fmv.x.{get_fl_flag(operands[1])}'

    def emit_riscv(self):
        dest, src = self.get_args()
        self.riscv_instructions += [
            f'{self.op} {dest}, {src}'
        ]


class FloatingPointConvert(Arm64Instruction):
    ''' Things like UCVTF, SCVTF -- converting from fixed point or integer
    '''
    opcodes = ['ucvtf', 'scvtf']

    def emit_riscv(self):
        unsigned = 'u' if self.opcode == 'ucvtf' else ''
        float_dest, integer_src = self.specific_regs
        wl = 'w' if is_half_width(self.operands[1]) else 'l'
        self.riscv_instructions = [
            f'fcvt.d.{wl}{unsigned} {float_dest}, {integer_src}'
        ]


class FloatingPointCompare(Arm64Instruction):
    ''' Floating point compare
    Requires a couple tricks to synthesize the compare result as an int.
    '''
    opcodes = ['fcmpe', 'fcmp']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.specific_regs.append(COMPARE)
        self.required_temp_regs = ['temp']  # we need the temp to get the two results in

    def emit_riscv(self):
        arg1, arg2, compare = self.specific_regs
        temp = self.required_temp_regs[0]

        self.riscv_instructions = [
            f'flt.d {compare}, {arg1}, {arg2} # this is less than, RHS is bigger',
            f'slli {compare}, {compare}, 63 # move it to the sign bit location',
            f'flt.d {temp}, {arg2}, {arg1} # if LHS is bigger',
            f'or {compare}, {compare}, {temp} # or the results together',
        ]


class FloatingPointSimplex(Arm64Instruction):
    """for the simple FP args -- 1:1
    """
    opcodes = ['fadd', 'fsub', 'fdiv', 'fmul', 'fmax', 'fmin']

    def emit_riscv(self):
        dst, s1, s2 = self.specific_regs
        self.riscv_instructions = [
            f'{self.opcode}.{self.fp_wflag} {dst}, {s1}, {s2}'
        ]


class FloatingPointSingleArg(Arm64Instruction):
    opcodes = ['fneg', 'fsqrt']

    def emit_riscv(self):
        dst, s1 = self.specific_regs
        self.riscv_instructions = [
            f'{self.opcode}.{self.fp_wflag} {dst}, {s1}'
        ]


class FloatingPointFused(Arm64Instruction):
    opcodes = ['fmadd', 'fmsub', 'fnmadd', 'fnmsub']

    opmap = {
        'fmadd': 'fmadd',
        'fnmadd': 'fnmadd',
        'fmsub': 'fnmsub',  # not sure why but fmsub and fnmsub are swapped in the syntax
        'fnmsub': 'fmsub',
    }

    def emit_riscv(self):
        dst, s1, s2, s3 = self.specific_regs
        self.riscv_instructions = [
            f'{self.opmap[self.opcode]}.{self.fp_wflag} {dst}, {s1}, {s2}, {s3}'
        ]


class AtomicLoadExclusive(Arm64Instruction):
    ''' LDAXR has a direct parallel -- LR = 'load-reserved' in RISC-V.
    This is an atomic.
    '''
    opcodes = ['ldaxr']

    def emit_riscv(self):
        dst, src = self.specific_regs
        size = 'w' if self.wflag else 'd'
        self.riscv_instructions = [
            f'lr.{size} {dst}, {self.offset}({src})'
        ]


class AtomicStoreExclusive(Arm64Instruction):
    ''' Atomic store ops - direct 1:1
    '''
    opcodes = ['stlxr']

    def emit_riscv(self):
        dst, desired, addr = self.specific_regs
        size = 'w' if self.wflag else 'd'
        self.riscv_instructions = [
            f'sc.{size} {dst}, {desired}, {self.offset}({addr})'
        ]


class LoadAcquireFence(Arm64Instruction):
    ''' LDAR is has an implicit fence semantic. We make it explicit here.
    '''
    opcodes = ['ldar']

    def emit_riscv(self):
        dst, src = self.specific_regs
        size = 'w' if self.wflag else 'd'
        self.riscv_instructions = [
            f'l{size} {dst}, {self.offset}({src})',
            f'fence iorw,iorw # making implicit fence semantics explicit',
        ]


class StoreReleaseFence(Arm64Instruction):
    ''' Atomic store ops - direct 1:1
    '''
    opcodes = ['stlr']

    def emit_riscv(self):
        desired, addr = self.specific_regs
        size = 'w' if self.wflag else 'd'
        self.riscv_instructions = [
            f'fence iorw,iorw  # making implicit fence semantics explicit',
            f's{size} {desired}, {self.offset}({addr})'
        ]


class AtomicOperations(Arm64Instruction):
    ''' Grouping together Arm64 Atomics, e.g. LDADD, CAS, etc.
    Translation is one to one op, with acquire-release semantics as well.
    '''
    opcodes = ['swp', 'ldadd', 'ldeor', 'ldset', 'ldsmin', 'ldsmax', 'ldumin', 'ldumax'] +\
        ['swpa', 'ldadda', 'ldeora', 'ldseta', 'ldsmina', 'ldsmaxa', 'ldumina', 'ldumaxa'] +\
        ['swpl', 'ldaddl', 'ldeorl', 'ldsetl', 'ldsminl', 'ldsmaxl', 'lduminl', 'ldumaxl'] +\
        ['swpal', 'ldaddal', 'ldeoral', 'ldsetal', 'ldsminal', 'ldsmaxal', 'lduminal', 'ldumaxal']

    opmap = {
        'swp': 'amoswap',
        'ldadd': 'amoadd',
        'ldeor': 'amoxor',
        'ldset': 'amoor',
        'ldsmax': 'amomax',
        'ldsmin': 'amomin',
        'ldumax': 'amomaxu',
        'ldumin': 'amominu',
    }

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        # key thing here: translate the acquire/release semantics
        if opcode.endswith('al'):  # acq + release
            self.suffix = '.aqrl'
        elif opcode.endswith('a'):
            self.suffix = '.aq'
        elif opcode.endswith('l'):
            self.suffix = '.rl'
        else:
            self.suffix = ''

        self.tr_opcode = self.opmap[opcode.rstrip('al')]

    def emit_riscv(self):
        size = 'w' if self.wflag else 'd'
        dst, desired, addr = self.specific_regs
        self.riscv_instructions = [
            f'{self.tr_opcode}.{size}{self.suffix} {desired}, {dst}, ({addr})'
        ]


class AtomicLoadAndClear(Arm64Instruction):
    opcodes = ['ldclr', 'ldclra', 'ldclrl', 'ldclral']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)
        self.required_temp_regs = ['temp']  # we will invert before the atomic
        # key thing here: translate the acquire/release semantics
        if opcode.endswith('al'):  # acq + release
            self.suffix = '.aqrl'
        elif opcode.endswith('a'):
            self.suffix = '.aq'
        elif opcode.endswith('l'):
            self.suffix = '.rl'
        else:
            self.suffix = ''

    def emit_riscv(self):
        size = 'w' if self.wflag else 'd'
        dst, desired, addr = self.specific_regs
        tmp = self.required_temp_regs[0]
        self.riscv_instructions = [
            f'not {tmp}, {dst}',
            f'amoand.{size}{self.suffix} {desired}, {tmp}, ({addr})'
        ]
