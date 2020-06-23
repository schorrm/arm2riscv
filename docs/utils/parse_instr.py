#!/usr/bin/python3

from lark import Lark
import sys
from pprint import pprint
sys.path.append('../../')

from convert_parse_tree import TreeToDict


if __name__ == "__main__":
    with open('../../grammar/grammar_arm.lark') as f:
        grammar = f.read()

    l = Lark(grammar, parser='earley')
    transformer = TreeToDict()

    fn = 'stm_ex.arm'
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    with open(fn) as f:
        lines = f.readlines()

    for line in lines:
        print()
        print(line.rstrip())
        tree = l.parse(line)
        d = transformer.transform(tree)
        print(tree.pretty())
        print()
        pprint(d)
        
