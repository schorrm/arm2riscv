# Testing Environment

## Setup

1. Install `riscv64-linux-gnu-gcc` and `aarch64-linux-gnu-gcc` from apt.

2. Copy the qemu static binaries to `/usr/local/bin`.

## Description

The full testing will come together later, but this will run the rough idea. There are basically going to be two types of testing.

1. From C code: armgcc -S -> arm2riscv -> rvgcc, and just rvgcc. Test both on qemu-static-riscv64, and check  that they are equivalent.

2. From Arm assembly: argmcc, and arm2riscv -> rvgcc. Test on qemue-static-aarch64 and qemu-static-riscv64, and check that they are equivalent.
