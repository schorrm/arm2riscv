#!/usr/bin/python3

from lark import Lark
import sys

if __name__ == "__main__":
    with open('grammar/grammar_arm.lark') as f:
        grammar = f.read()

    l = Lark(grammar, parser='earley')

    fn = 'stm_ex.arm'
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    with open(fn) as f:
        lines = f.readlines()

    for line in lines:
        print()
        print(line.rstrip())
        x = l.parse(line)
        print(x.pretty())
        print()
        print(type(x))
        
