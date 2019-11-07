#!/usr/bin/python3

# The initial component: convert a file to a dict representation of the machine code

from lark import Lark, Transformer
from convert_parse_tree import TreeToDict
import sys

transformer = TreeToDict()

with open('grammar/grammar_arm.lark') as f:
    grammar = f.read()

l = Lark(grammar, parser='earley')


ops = set()
for line in sys.stdin:
    tree = l.parse(line)
    print()
    print(line)
    d = transformer.transform(tree)
    print(d)
    print()

    if 'operation' in d.keys():
        ops.add(d['operation']['opcode'])

for i, o in enumerate(ops, 1):
    print(i, o, sep='\t')