#!/usr/bin/env python
import argparse
import sys
from acyclic import CCodeParser

argparser = argparse.ArgumentParser(description='Acyclic Path Analyser')
argparser.add_argument('--trace', action="store_true")
args = argparser.parse_args()

text=''
for line in sys.stdin:
    text += line

parser=CCodeParser(text)
parser.parse()

if args.trace:
    for d in parser.getDecisions():
        print(d, end='')
        scope = d.getParent()
        while scope:
            print(' \\ ', end='')
            print(scope, end='')
            scope = scope.getParent()
        print()

print(parser.complexity())
