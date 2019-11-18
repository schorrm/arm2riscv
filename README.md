# arm2riscv

Arm AArch64 to RISC-V Transpiler

## Usage

`armgcc -S -o - <input file name> | python3 arm2riscv.py | rvgcc -x assembler - -static`

Or use:

`./compile_thru_arm2riscv.sh <file name>`

## Test Suite

`python3 test_suite.py` runs the testing.

## Dependencies

- Lark
- tqdm (tests)
