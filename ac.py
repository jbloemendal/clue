#!/usr/bin/env python
import fileinput
from acyclic import CCodeParser

text=''
for line in fileinput.input():
    text += line

parser=CCodeParser(text)
parser.parse()

for d in parser.getDecisions():
    print(d, end='')
    scope = d.getParent()
    while scope:
        print(' \\ ', end='')
        print(scope, end='')
        scope = scope.getParent()
    print()

print(parser.complexity())
