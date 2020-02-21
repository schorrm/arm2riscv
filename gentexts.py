#!/usr/bin/python3

import sys
import os
import subprocess
from tqdm import tqdm
import glob

from tabulate import tabulate

import pandas as pd

TEXT_DIR = 'testing/texts'
CODE_DIR = 'testing/code'
if not os.path.isdir(TEXT_DIR):
    os.mkdir(TEXT_DIR)

code_files = glob.glob(f'{CODE_DIR}/*.c')

success = 0
total = len(code_files)

logfile = f'{TEXT_DIR}/instruction_log.csv'
logtable = f'{TEXT_DIR}/instruction_log.md'

if os.path.exists(logfile):
    os.remove(logfile)

for fn in tqdm(code_files):
    text_base = fn.split('/')[-1].split('.')[0]
    text_path = f'{TEXT_DIR}/{text_base}'

    c_r = subprocess.check_call(
        f'aarch64-linux-gnu-gcc -march=armv8.3-a -S -o - {fn}'  # make Arm64 assembly
        f'| python3 arm2riscv.py -annot -xnames --logfile {logfile}'  # transpile
        f'> {text_path}.asm',  # linker stage
        shell=True)

df = pd.read_csv(logfile, names=['Opcode', 'Instruction', 'Translation'])
df.sort_values('Opcode', inplace=True)
df = df.drop_duplicates(subset=['Opcode'])
df.reset_index(inplace=True, drop=True)
for col in ['Opcode', 'Instruction']:
    df[col] = [f'`{x}`' for x in df[col]]
df['Translation'] = [f'```{x}```' for x in df.Translation]
table = tabulate(df, tablefmt='github')
with open(logtable, 'w') as f:
    f.write(table)