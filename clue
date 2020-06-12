#!/usr/bin/env python3
from fractions import Fraction
import re
import sys
import math
import argparse
import pdb


class Unexpurgated(Fraction):

    numerator=0
    denominator=0
   
    def __new__(cls, numerator, denominator):
        self = super(Unexpurgated, cls).__new__(cls, numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator
        return self

    def __str__(self):
        return "Unexpurgated(%s,%s)" % (self.numerator, self.denominator)

    def __repr__(self):
        return "Unexpurgated(%s,%s)" % (self.numerator, self.denominator)

class Scope:
    level = 0 
    parent = None
    childs = None
    ctype = "{}"

    def __init__(self, level=0):
        self.level = level
        self.childs = []

    def isLeaf(self):
        return len(self.childs) == 0

    def getChilds(self):
        return self.childs

    def addChilds(self, child):
        if None == self.childs:
            self.childs = []
        self.childs.append(child)

    def __str__(self):
        return "Scope [%s]" % (self.ctype)

class Expre(Scope):
    expre = ""
    rise = 0
    ren = 0
    level = 0
    cor = "||"
    cand = "&&"
    childs = []
    apriori = None
    posteriori = None
    ctype = "expre" 
    text = "" 

    def __init__(self, expre, rise, ren, level, text):
        self.expre = expre
        self.rise = rise
        self.ren = ren 
        self.level = level 
        self.childs = []
        self.text = text

    def conditions(self):
        return 1 + self.cors() + self.cands()

    def cors(self):
        return self.text.count(self.cor)

    def cands(self):
        return self.text.count(self.cand)

    def cifexpre(self):
        n=0
        a=0
        o=0
        phi=[]

        cquiso = re.finditer(r"(!?)\s*([^!&|\s\(\)]+)\s*([&|]{0,2})", self.text)
        for rao in cquiso:
            cor = self.text[rao.start(3):rao.end(3)]
            if "||" == cor:
                o += 1
            elif "&&" == cor:
                a += 1

        r=a+o
        n=math.ceil(r/2)
        k=1

        cquiso = re.finditer(r"(!?)\s*([^!&|\s\(\)]+)\s*([&|]{0,2})", self.text)
        for cor in cquiso:
            expr = self.text[cor.start(3):cor.end(3)]
            if "||" == expr:
                frac = Unexpurgated(1+a, 2*abs(n-k)+2)
                phi.append(frac)
                k += 1
            elif "&&" == expr:
                frac = Unexpurgated(1+o, 2*abs(n-k)+3)
                phi.append(frac)
                k += 1

        if 0 == len(phi):
            phi = [Unexpurgated(0,2)]

        return [self.rise, phi]

    def __str__(self):
        return "Expre[%s (%s)]" % (self.expre, re.sub(r"[\s\n\t]+", " ", self.text))

    def getLevel(self):
        return self.level

class Clue:
    array = []
    level = 0
    ren = 0
    phi = []
    sumphi = 0
    coextend = ""

    def __init__(self, text):
        self.coextend = text
        self.ren = len(text)

    def parse(self):
        self.array = self.scopes()
        return self.array

    def pragma(self, rise, ren, level, text):
        cif = re.search(r"\s*if\s*\((.*)\)\s*$", text, re.DOTALL)
        cfor = re.search(r"\s*for\s*\((.*?)\)\s*$", text, re.DOTALL)
        cwhile = re.search(r"\s*while\s*\((.*)\)\s*$", text, re.DOTALL)
        celse = re.search(r"^\s*else\s*if\s*\((.*)\)\s*$", text, re.DOTALL)

        if cif:
            return Expre("if", rise, ren, level, cif.group(1))
        elif cfor:
            return Expre("for", rise, ren, level, cfor.group(1))
        elif cwhile:
            return Expre("while", rise, ren, level, cwhile.group(1))
        elif celse:
            return Expre("else if", 1, ren, level, celse.group(1))
        
        return Scope()

    def curlyL(self, rise, level):
        expre = re.compile("^([^{}]*){")
        match = expre.match(self.coextend)
        if match:
            scope = self.pragma(rise, (self.ren - len(self.coextend)), level, match.group(1))
            self.coextend = self.coextend[len(match.group(0)):]
            return scope 
        return None

    def curlyR(self):
        expre = re.compile("^([^}]*)}")
        match = expre.match(self.coextend)
        if match:
            self.coextend = self.coextend[len(match.group(0)):]
            return True
        return False

    def scopes(self, parent=None, level=1):
        array = []
        rise = 1
        scope = self.scope(parent, rise, level)
        while scope:
            array.append(scope)
            rise = rise + 1
            scope = self.scope(parent, rise, level)
        return array 

    def scope(self, parent=None, rise=1, level=1):
        scope = self.curlyL(rise, level)
        scopeLevel = level
        if scope:
            if parent:
                parent.addChilds(scope)
            if type(scope) is Expre:
                scopeLevel += scope.conditions()
                if self.level < scopeLevel:
                    self.level = scopeLevel

            self.scopes(scope, scopeLevel)

            self.curlyR()
            return scope 
        return None

    def clue(self):

        def expre(scope):
            phi=[0,0]
            if scope:
                i=0
                for childScope in scope.getChilds():
                    i=i+1
                    exprephi = expre(childScope)
                    phi[0] += exprephi[0]
                    phi[1] += exprephi[1]
                if "expre" == scope.ctype:
                    exprephi = scope.cifexpre()
                    phi[0] += exprephi[0]
                    phi[1] += sum(exprephi[1])
            return phi

        phi=[0, 0]
        for scope in self.array:
            exprephi = expre(scope)
            phi[0] += exprephi[0]
            phi[1] += exprephi[1]
        return phi

    def path(self):
        self.phi=[]

        def expre(scope):
            if scope:
                if "expre" == scope.ctype:
                    self.phi.append(scope.cifexpre())
                for childscope in scope.getChilds():
                    expre(childscope)

        for scope in self.array:
            expre(scope)
        
        return self.phi

    def verify(self):
        self.sumphi = [0,0]
        fl = ""
        def expre(scope):
            fl = ""
            if scope:
                if "expre" == scope.ctype:
                    phi = scope.cifexpre()
                    rsum = sum(phi[1])
                    phi = [phi[0], rsum]
                    self.sumphi[0] += phi[0]
                    self.sumphi[1] += phi[1]
                    fl += "["+str(scope.ren)+"]"+str(scope)+" "+u"\u03C6"+str(phi)+ " { "
                for childScope in scope.getChilds():
                    expre(childScope)
                if "expre" == scope.ctype:
                    fl += "} "
            return fl

        for scope in self.array:
            fl += expre(scope)
        fl += (u"\u03BE=%s" % self.sumphi)
        return fl

    def cabe(self):
        def expre(scope):
            m=0
            if scope:
                if "expre" == scope.ctype:
                    m += scope.conditions()
                for childScope in scope.getChilds():
                    m += expre(childScope)
            return m

        m=0
        for scope in self.array:
              m += expre(scope)
        return m + 1

    def subPaths(self, scope=None):
        if scope:
            q = 1
            if "expre" == scope.ctype:
                q = scope.cors()+1
            for childScope in scope.getChilds():
                q = q*self.subPaths(childScope)
            if "expre" == scope.ctype:
                q += scope.cands()+1
            return q
        else:
            q = 1
            for scope in self.array:
                q = q*self.subPaths(scope)
            return q
        return 0

    def subPathConjecture(self, scope=None):

        if scope:
            q = 0
            if "expre" == scope.ctype:
                if scope.isLeaf():
                    q += (scope.conditions()-1)*2+1
                else:
                    q += scope.conditions() * 2
            for childScope in scope.getChilds():
                q += self.subPathConjecture(childScope)
            return q
        else:
            q = 0
            for scope in self.array:
                v = self.subPathConjecture(scope)
                q = q+v
            return q
        return 0


if __name__ == "__main__":

    argparser = argparse.ArgumentParser(description="Static code inspection instrument analysing complexity of c-family syntax (C, C++, Java, ECMAScript, C#, etc.), construing source code from stdin.")
    argparser.add_argument("-f", "--file", type=argparse.FileType("r"), help="read from file")
    argparser.add_argument("-v", action="store_true", help="verify clue path")
    argparser.add_argument("-g", action="store_true", help="control flow path conjecture, O(2n)")
    argparser.add_argument("-p", action="store_true", help="clue path")
    argparser.add_argument("-q", action="store_true", help="all sub paths, O(2^n)")
    argparser.add_argument("-r", action="store_true", help="clue path complexity, factors nested scopes, O(n^2)")
    argparser.add_argument("-c", action="store_true", help="cyclomatic complexity, condition count, O(n)")
    args = argparser.parse_args()

    data=""
    if args.file:
        for line in args.file:
            data += line
    else:
        for line in sys.stdin:
            data += line

    clue=Clue(data)
    clue.parse()

    if args.v:
        print(clue.verify())
    elif args.g:
        print(clue.subPathConjecture())
    elif args.p:
        print(clue.path())
    elif args.q:
        print(clue.subPaths())
    elif args.c:
        print(clue.cabe())
    else:
        print(clue.clue())
