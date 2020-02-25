#!/usr/bin/python3

# RISC-V opcode parser for debugging

import argparse


def print_fields(revbs, fields):
    cbase = 0
    for field, flen in fields:
        curr = revbs[cbase:cbase+flen]
        ix = f'({int(curr, 2)})'
        print(f'{field:12} {ix:7} {curr}')
        cbase += flen


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("format", help="which instruction format?")
arg_parser.add_argument('value', help="the opcode in hexadecimal")

args = arg_parser.parse_args()

if args.format == 'B':
    val = int(args.value, 16)
    bin_str = f'{val:032b}'

    # note: this reads in the opposite direction
    lookup = bin_str[::-1]

    print_fields(lookup, [
        ('opcode', 7),
        ('imm[11]', 1),
        ('imm[4:1]', 4),
        ('funct3', 3),
        ('rs1', 5),
        ('rs2', 5),
        ('imm[10:5]', 6),
        ('imm[12]', 1), ]
    )
