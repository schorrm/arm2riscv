#!/usr/bin/python3

import sys
import os
import subprocess
from tqdm import tqdm

BIN_DIR = 'testing/bin'
CODE_DIR = 'testing/code'
if not os.path.isdir(BIN_DIR):
    os.mkdir(BIN_DIR)

success = 0
total  = len(os.listdir(CODE_DIR))

for fn in tqdm(os.listdir(CODE_DIR)):
    fp = f'{CODE_DIR}/{fn}'
    bin_base = fn.split('.')[0]
    bin_path = f'{BIN_DIR}/{bin_base}'

    c_r = subprocess.check_call(f'aarch64-linux-gnu-gcc -S -o - {fp} | python3 arm2riscv.py | riscv64-linux-gnu-gcc -x assembler - -static -o {bin_path}_transpiled.out', shell=True)

    if c_r != 0:
        print ('failed on build', fn)
        exit(1)

    subprocess.check_call(f'riscv64-linux-gnu-gcc {fp} -static -o {bin_path}_basic.out', shell=True)
    transpiled = subprocess.check_output(f'qemu-riscv64-static {bin_path}_transpiled.out', shell=True)
    basic = subprocess.check_output(f'qemu-riscv64-static {bin_path}_basic.out', shell=True)

    if transpiled == basic:
        success += 1
    else:
        print('failed test', fn)

print(f'Passed {success} / {total} tests')