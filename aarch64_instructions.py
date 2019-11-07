#!/usr/bin/python3

"""
Classes:
LoadRegisterByte
UnsignedMultiplyAddLong

"""


class ArmInstruction:
    def __init__(self):
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
                'LB {dest} , {offset}({src})'
            ]
            if writeback:
                self.riscv_instructions.append([
                    'ADDI {src}, {offset}'
                ])
        else:
            self.riscv_instructions = [
                'LB {dest}, ({src})'
            ]        
    
class UnsignedMultiplyAddLong(ArmInstruction):
    opcodes = ['umaddl']

    def __init__(self, operands):
        super().__init__()
        dest = operands[0]
        wm, wn, xa = operands[1:4]
        self.required_temp_regs = ['temp']
        self.specific_regs = [dest, wm, wn, xa]

    def emit_riscv(self):
        temp = self.temp_regs[0]
        dest, wm, wn, xa = self.specific_regs
        self.riscv_instructions = [
            f'MULW {temp}, {wm}, {wn}',
            f'ADD {dest}, {xa}, {temp}'
        ]
        
        
    