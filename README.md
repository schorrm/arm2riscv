# arm2riscv

Arm AArch64 to RISC-V Transpiler

## Usage

`armgcc -S -o - <input file name> | python3 arm2riscv.py | rvgcc -x assembler - -static`

Or use:

`./compile_thru_arm2riscv.sh <file name>`

Run `python3 arm2riscv.py -h` for fuller usage and flags.

## Test Suite

`python3 test_suite.py` runs the testing.

## Setup:

*Requires: Python 3.6 or newer*

You can use the [dockerfile](testing/setup_environment.dockerfile), or manually set up a test environment. 

### Python Dependencies

- lark-parser (`pip install lark-parser`)
- tqdm (tests) (`pip install tqdm`)

### Compilers

The safest option is to stick to the tested versions on Ubuntu, since both were tested on version 7.4.0.
Both compiler toolchains are needed to run the test suite. Run:

- `sudo apt-get install gcc-aarch64-linux-gnu=4:7.4.0-1ubuntu2.3`
- `sudo apt-get install gcc-riscv64-linux-gnu=4:7.4.0-1ubuntu1.3`

### Qemu

Since the correct qemu-static-user binaries are hard to find, they're included.
Copy both of them (`qemu-aarch64-static`, `qemu-riscv64-static`) from `testing/qemu_binaries` to `/usr/local/bin` so they're visible to the testing.

Tests should now be runnable -- `python3 test_suite.py` in the main directory should be able to run it.
