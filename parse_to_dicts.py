#!/usr/bin/python3

# The initial component: convert a file to a dict representation of the machine code

from lark import Lark, Transformer
from convert_parse_tree import TreeToDict
import sys

transformer = TreeToDict()

with open('grammar/grammar_arm.lark') as f:
    grammar = f.read()

l = Lark(grammar, parser='earley')

for line in sys.stdin:
    tree = l.parse(line)
    
    print()
    print(line)
    print(transformer.transform(tree))
    print()