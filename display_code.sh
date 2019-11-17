#!/bin/bash
#echo "AArch Input"
#aarch64-linux-gnu-gcc -S -o - $1

#echo ""
#echo "Transpiled"
aarch64-linux-gnu-gcc -S -o - $1 | python3 arm2riscv.py
