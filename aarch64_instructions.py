#!/usr/bin/python3

"""
Classes:
LDRB LoadRegisterByte
UMADDL UnsignedMultiplyAddLong
BL BranchAndLink
ADRP AddressPCRelative
MOV Move
"""


class ArmInstruction:
    def __init__(self, operands):
        self.riscv_instructions = []

    def emit_riscv(self) -> List[str]:
        return self.riscv_instructions
    
class LoadRegisterByte(ArmInstruction):
    opcodes = ['ldrb']

    def __init__(self, operands):
        super().__init__()
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
    
class UnsignedMultiplyAddLong(ArmInstruction):
    opcodes = ['umaddl']

    def __init__(self, operands):
        super().__init__()
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
        
        
class BranchAndLink(ArmInstruction):
    opcodes = ['bl']

    def __init__(self, operands):
        super().__init__()
        label = operands[0]
        self.riscv_instructions = [
            f'call {label}'
        ]

class AddressPCRelative(ArmInstruction):
    opcodes = ['adrp']

    def __init__(self, operands):
        super().__init__()
        dest = operands[0]['register']
        self.specific_regs = [dest]
        self.label = operands[1]['label']


    def emit_riscv(self):
        dest = self.specific_regs[0]
        self.riscv_instructions = [
            f'lui {dest} %hi%({self.label})'
        ]

class Move(ArmInstruction):
    opcodes = ['mov']

    def __init__(self, operands):
        super().__init__()
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