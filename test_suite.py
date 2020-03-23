#!/usr/bin/python3

import sys
import os
import subprocess
from tqdm import tqdm
import glob

BIN_DIR = 'testing/bin'
CODE_DIR = 'testing/code'
if not os.path.isdir(BIN_DIR):
    os.mkdir(BIN_DIR)

code_files = glob.glob(f'{CODE_DIR}/*.c')

success = 0
total = len(code_files)

for fn in tqdm(code_files):
    bin_base = fn.split('/')[-1].split('.')[0]
    bin_path = f'{BIN_DIR}/{bin_base}'

    c_r = subprocess.check_call(
        f'aarch64-linux-gnu-gcc -march=armv8.3-a -S -o - {fn}'  # make Arm64 assembly
        f'| python3 arm2riscv.py'  # transpile
        f'| riscv64-linux-gnu-gcc -x assembler - -pthread -static -o {bin_path}_transpiled.out',  # linker stage
        shell=True)

    if c_r != 0:
        print('failed on build', fn)
        exit(1)

    tflag = '-pthread' if 'thread' in fn else ''
    

    subprocess.check_call(f'aarch64-linux-gnu-gcc {fn} -march=armv8.3-a -static {tflag} -o {bin_path}_basic.out', shell=True)
    transpiled = subprocess.check_output(f'qemu-riscv64-static {bin_path}_transpiled.out', shell=True)
    basic = subprocess.check_output(f'qemu-aarch64-static {bin_path}_basic.out', shell=True)

    if transpiled == basic:
        success += 1
    else:
        tqdm.write(f'failed test {fn}')
        # diffs.append([fn, basic, transpiled])

print(f'Passed {success} / {total} tests')

# for fn, reference, transpiled in diffs:
#     print(f'Failed test: {fn}')
#     print('Should have been:')
#     print(str(reference))
#     print('Was:')
#     print(str(transpiled))
