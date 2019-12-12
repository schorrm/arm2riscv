#!/usr/bin/python3

import sys
import os
import subprocess
from tqdm import tqdm

TEXT_DIR = 'texts'
CODE_DIR = 'testing/code'
if not os.path.isdir(TEXT_DIR):
    os.mkdir(TEXT_DIR)

success = 0
total  = len(os.listdir(CODE_DIR))

for fn in tqdm(os.listdir(CODE_DIR)):
    fp = f'{CODE_DIR}/{fn}'
    text_base = fn.split('.')[0]
    text_path = f'{TEXT_DIR}/{text_base}.txt'

    c_r = subprocess.check_output(f'aarch64-linux-gnu-gcc -S -o - {fp} | python3 arm2riscv.py -annot', shell=True)
    # c_r = str(c_r)
    with open(text_path, 'wb') as f:
        f.write(c_r)

print(f'Printed {total} texts')