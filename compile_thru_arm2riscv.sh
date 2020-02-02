#!/bin/bash

aarch64-linux-gnu-gcc -march=armv8.3-a -S -o - $1 | python3 arm2riscv.py | riscv64-linux-gnu-gcc -static $2 -x assembler - 