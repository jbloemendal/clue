#!/usr/bin/env python
import argparse
import sys
from measure import CCodeParser

argparser = argparse.ArgumentParser(description='Code Complexity Measure')
argparser.add_argument('-t', '--trace', action="store_true")
argparser.add_argument('-c', '--cabe', action="store_true")
argparser.add_argument('-a', '--acyc', action="store_true")
args = argparser.parse_args()

text=''

for line in sys.stdin:
    text += line

par=CCodeParser(text)
par.parse()
if args.trace:
    par.trace()

if args.cabe:
    print(par.cabe())
else:
    print(par.acyc())
