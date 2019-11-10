# arm2riscv

Arm AArch64 to RISC-V Transpiler

## Usage

`armgcc -S -o - <input file name> | python3 arm2riscv.py | rvgcc -x assembler - -static`

## Test Suite

`python3 test_suite.py` runs the testing.

## Dependencies

- Lark
- tqdm (tests)
