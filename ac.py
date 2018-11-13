#!/usr/bin/env python
import fileinput
from acyclic import CCodeParser

text=''
for line in fileinput.input():
    text += line

parser=CCodeParser(text)
parser.parse()

for d in parser.decisions():
    print(d)
print(parser.complexity())
