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

    def __repr__(self):
        return "Unexpurgated(%s,%s)" % (self.numerator, self.denominator)

    def __str__(self):
        return "Unexpurgated(%s,%s)" % (self.numerator, self.denominator)

class Scope:
    level = 0 
    parent = None
    childs = None
    ctype = "{}" # class, function (func), flow, encapsulation ({})

    def __init__(self, level=0):
        print("Scope __init__")
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
    clen = 0
    level = 0
    cand = "&&"
    cor = "||"
    childs = []
    apriori = None
    posteriori = None
    ctype = "expre" # desicion \ attor, find apriori \ posteriori
    text = "" 

    def __init__(self, expre, rise, clen, level, text):
        self.expre = expre
        self.rise = rise
        self.clen = clen 
        self.level = level 
        self.text = text
        self.childs = []

    def cors(self):
        return self.text.count(self.cor)

    def cands(self):
        return self.text.count(self.cand)

    def conditions(self):
        return 1 + self.cors() + self.cands()

    def cifexpre(self):
        pdb.set_trace()
        print("cifexpre %s" % self);
        n=0
        a=0
        o=0

        phi=[]

        print("rise:%s, level: %s, (%s) " % (self.rise, self.level, self.text))
        cquiso = re.finditer(r"(!?)\s*([^!&|\s\(\)]+)\s*([&|]{0,2})", self.text) # 1:! 2:variable 3: &&||
        for rao in cquiso:
            cor = self.text[rao.start(3):rao.end(3)]
            if "&&" == cor:
                a += 1
            elif "||" == cor:
                o += 1
        print("a %s, o %s" % (a,o))

        r=a+o
        n=math.ceil(r/2)
        k=1
        print("r %s, n %s, k %s" % (r, n, k))
        cquiso = re.finditer(r"(!?)\s*([^!&|\s\(\)]+)\s*([&|]{0,2})", self.text)
        for cor in cquiso:
            expr = self.text[cor.start(3):cor.end(3)]
            if "&&" == expr:
                pdb.set_trace()
                print("&& %s/%s" % (1.0+o, 2.0*abs(n-k)+3)) #, end=", ")
                frac = Unexpurgated(1+o, 2*abs(n-k)+3)
                phi.append(frac)
                k += 1
            elif "||" == expr:
                pdb.set_trace()
                print("%s: r: %s, n:%s, k:%s, a:%s o:%s " % (expr, r, n, k, a, o)) #, end="")
                frac = Unexpurgated(1+a, 2*abs(n-k)+2)
                phi.append(frac)
                k += 1

        print("")
        if 0 == len(phi):
            phi = [Unexpurgated(0,2)]

        return [self.rise, phi]

    def getLevel(self):
        return self.level

    def __str__(self):
        return "Expre[%s (%s)]" % (self.expre, re.sub(r"[\s\n\t]+", " ", self.text))

class Clue:

    level = 0
    array = []
    ren = 0
    coextend = ""
    phi = []
    sumphi = 0

    def __init__(self, text):
        self.ren = len(text)
        self.coextend = text

    def parse(self):
        print("parse");
        self.array = self.scopes()
        return self.array

    def pragma(self, rise, ren, level, text):
        print("pragma %s ren, rise %s, level %s, text %s" % (ren, rise, level, text))
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
        print("curlyL coextend %s" % self.coextend)
        expre = re.compile("^([^{}]*){")
        match = expre.match(self.coextend)
        if match:
            scope = self.pragma(rise, (self.ren - len(self.coextend)), level, match.group(1))
            self.coextend = self.coextend[len(match.group(0)):]
            return scope 
        return None

    def curlyR(self):
        print("curlyR")
        expre = re.compile("^([^}]*)}")
        match = expre.match(self.coextend)
        if match:
            self.coextend = self.coextend[len(match.group(0)):]
            return True
        return False

    def scopes(self, parent=None, level=1):
        print("scopes parent %s level %s" % (parent, level))
        array = []
        rise = 1
        scope = self.scope(parent, rise, level)
        while scope:
            array.append(scope)
            rise = rise + 1
            scope = self.scope(parent, rise, level)
            print("rise %s, level %s" % (rise, level))
        return array 

    def scope(self, parent=None, rise=1, level=1):
        print("scope parent %s rise %s level %s" % (parent, rise, level))
        scope = self.curlyL(rise, level)
        scopeLevel = level
        if scope:
            if parent:
                pdb.set_trace()
                scope.addChilds(parent)
            if type(scope) is Expre:
                scopeLevel += scope.conditions()
                if self.level < level:
                    self.level = level

            self.scopes(scope, level)

            self.curlyR()
            return scope 
        return None

    def clue(self):

        print("!clue")
        def expre(scope):
            print("clue\expression %s" % (scope))
            phi=[0,0]
            if scope:
                print("expre scope %s, children length %s " % (scope, len(scope.getChilds())))
                i=0
                for childScope in scope.getChilds():
                    i=i+1
                    print("childscope %s" % childScope)
                    exprephi = expre(childScope)
                    phi[0] += exprephi[0]
                    phi[1] += exprephi[1]
                if "expre" == scope.ctype: #attcupor expre
                    print("expre")
                    exprephi = scope.cifexpre()
                    phi[0] += exprephi[0]
                    phi[1] += sum(exprephi[1])
            return phi

        phi=[0, 0]
        for scope in self.array:
            print("scope in array")
            pdb.set_trace()
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
                    fl += "["+str(scope.fluo)+"]"+str(scope)+" "+u"\u03C6"+str(phi)+ " { "
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
                q = scope.ors()+1 # scope entrances
            for childScope in scope.getChilds():
                q = q*self.subPaths(childScope)
            if "expre" == scope.ctype:
                q += scope.ands()+1 # False exits
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
            print("scope %s, or %s, and %s, leaf: %s" % (scope.text, scope.ors(), scope.ands(), scope.isLeaf()))
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

    argparser = argparse.ArgumentParser(description="Static code inspection instrument analysing complexity of c-family syntax (C, C++, Java, ECMAScript, C#, ...), construing source code of a standard data input streams (stdin) into absolute measures.")
    argparser.add_argument("-c", action="store_true", help="cyclomatic complexity, condition count, O(n)")
    argparser.add_argument("-f", "--file", type=argparse.FileType("r"), help="read one or more newline separated lines from file")
    argparser.add_argument("-g", action="store_true", help="control flow path conjecture O(2n)")
    argparser.add_argument("-k", action="store_true", help="clue path complexity, regards nested c-family syntax, O(n^2)")
    argparser.add_argument("-p", action="store_true", help="clue path")
    argparser.add_argument("-q", action="store_true", help="all sub paths, O(2^n)")
    argparser.add_argument("-v", action="store_true", help="verify clue path")
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
    elif args.p:
        print(clue.path())
    elif args.q:
        print(clue.subPaths())
    elif args.g:
        print(clue.subPathConjecture())
    elif args.c:
        print(clue.cabe())
    else:
        print(clue.clue())
