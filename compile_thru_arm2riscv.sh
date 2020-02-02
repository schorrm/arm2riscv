#!/bin/bash

aarch64-linux-gnu-gcc -S -o - $1 | python3 arm2riscv.py | riscv64-linux-gnu-gcc -static $2 -x assembler - 