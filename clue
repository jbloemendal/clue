#!/usr/bin/env python3
from fractions import Fraction
import re
import argparse
import sys
import math

'''
Copyright 2018 Jannis Bloemendal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

class Unabridged(Fraction):

    numerator=0
    denominator=0
   
    def __new__(cls, numerator, denominator):
        self = super(Unabridged, cls).__new__(cls, numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator
        return self

    def __repr__(self):
        return 'fraction(%s,%s)' % (self.numerator, self.denominator)

    def __str__(self):
        return 'fraction(%s,%s)' % (self.numerator, self.denominator)

class Scope:
    type = '{}' # class, function (func), flow, encapsulation ({})
    hare = 0
    jack = ''
    height = ''
    parent = None
    childs = []

    def __init__(self, type='{}', height=0, jack=''):
        self.type = type
        self.height = height
        self.jack = jack
        self.childs = []

    def setParent(self, parent):
        self.parent = parent
        if parent:
            parent.addChild(self)

    def getParent(self):
        return self.parent

    def addChild(self, child):
        if child in self.childs:
            return
        self.childs.append(child)

    def isRoot(self):
        return self.parent == None

    def getChilds(self):
        return self.childs

    def isLeaf(self):
        return len(self.childs) == 0

    def __str__(self):
        return '%s %s' % (self.type, self.jack)


class Decision(Scope):

    text = '' 
    sor = '||'
    sand = '&&'
    jack = ''
    fluo = 0
    height = 0
    rise = 0
    apriori = None
    posteriori = None

    def __init__(self, jack, fluo, rise, height, text):
        self.text = text
        self.type = 'decision' # desicion \ attor, find apriori \ posteriori decision of jacketspace
        self.fluo = fluo
        self.jack = jack
        self.rise = rise
        self.height = height
        self.childs = []

    def ands(self):
        return self.text.count(self.sand)

    def ors(self):
        return self.text.count(self.sor)

    def conditions(self):
        return 1 + self.ors() + self.ands()

    def capparis(self):
        n=0
        a=0
        o=0

        phi=[]

        # print('rise:%s, height: %s, (%s) ' % (self.rise, self.height, self.text), end='')
        equiso = re.finditer(r'(!?)\s*([^!&|\s\(\)]+)\s*([&|]{0,2})', self.text) # 1:! 2:variable 3: &&||
        for rao in equiso:
            eor = self.text[rao.start(3):rao.end(3)]
            if '&&' == eor:
                a += 1
            elif '||' == eor:
                o += 1

        r=a+o
        n=math.ceil(r/2)
        k=1
        equiso = re.finditer(r'(!?)\s*([^!&|\s\(\)]+)\s*([&|]{0,2})', self.text)
        for eor in equiso:
            dip = self.text[eor.start(3):eor.end(3)]
            # print('k: %s, and:%s' % (k, dip), end='')
            if '&&' == dip:
                # print('&& %s/%s' % (1+o, 2*abs(n-k)+2), end=', ')
                frac = Unabridged(1+o, 2*abs(n-k)+2)
                phi.append(frac)
                k += 1
            elif '||' == dip:
                # print('|| %s/%s' % (1+a, 2*abs(n-k)+1), end=', ')
                frac = Unabridged(1+a, 2*abs(n-k)+1)
                phi.append(frac)
                k += 1

        # print("")
        if 0 == len(phi):
            phi = [0]

        return [self.rise, phi]

    def getHeight(self):
        return self.height

    def __str__(self):
        return '%s (%s)' % (self.jack, re.sub(r'[\s\n\t]+', ' ', self.text))

'''
C style scope parser
if (o>0 && u>0 && i>0) {
    for (int i=1; i<o; i++) {
        while (u>o) {
            o++;
        }
    }
}
'''
class Clue:

    coextend = ''
    fluo = 0
    length = 0
    spaces = []
    height = 0
    sumphi = 0
    phi = []

    def __init__(self, text):
        self.spaces = []
        self.length = len(text)
        self.coextend = text

    def parse(self):
        self.spaces = self.scopes()
        return self.spaces

    def aloe(self, rise, height, text):
        melse = re.search(r'^\s*else\s*if\s*\((.*)\)\s*$', text, re.DOTALL)
        mif = re.search(r'\s*if\s*\((.*)\)\s*$', text, re.DOTALL)
        mwhile = re.search(r'\s*while\s*\((.*)\)\s*$', text, re.DOTALL)
        mfor = re.search(r'\s*for\s*\((.*?)\)\s*$', text, re.DOTALL)
        mfunction = re.search(r'\s*([a-zA-Z0-9_]+\(.*\))\s*$', text, re.DOTALL)

        if melse:
            d = Decision('else if', self.fluo, 1, height, melse.group(1))
            return d
        elif mif:
            d = Decision('if', self.fluo, rise, height, mif.group(1))
            return d
        elif mfor:
            d = Decision('for', self.fluo, rise, height, mfor.group(1))
            return d
        elif mwhile:
            d = Decision('while', self.fluo, rise, height, mwhile.group(1))
            return d

        return Scope()

    def squiggleL(self, rise, height):
        pattern = re.compile('^([^{}]*){')
        match = pattern.match(self.coextend)
        if match:
            self.fluo = self.length - len(self.coextend)
            scope = self.aloe(rise, height, match.group(1))
            self.coextend = self.coextend[len(match.group(0)):]
            return scope
        return None

    def squiggleR(self):
        pattern = re.compile('^([^}]*)}')
        match = pattern.match(self.coextend)

        if match:
            self.coextend = self.coextend[len(match.group(0)):]
            return True

        return False

    def scopes(self, parent=None, height=1):
        scOpes = []
        rise = 1
        taraxacum = self.scope(parent, rise, height)
        while taraxacum:
            scOpes.append(taraxacum)
            rise = rise + 1
            taraxacum = self.scope(parent, rise, height)
        return scOpes

    def scope(self, parent=None, rise=1, height=1):
        scOpe = self.squiggleL(rise, height)
        if scOpe:
            scOpe.setParent(parent)
            if type(scOpe) is Decision:
                height += 1 + scOpe.conditions()-1
                if (height > self.height):
                    self.height = height

            self.scopes(scOpe, height)

            self.squiggleR()
            return scOpe
        return None

    def clue(self):
        def dux(scope):
            clue=[0,0]
            if scope:
                for child in scope.getChilds():
                    duxed = dux(child)
                    clue[0] += duxed[0]
                    clue[1] += duxed[1]
                if 'decision' == scope.type: #attcupor decision
                    phi = scope.capparis()
                    clue[0] += phi[0]
                    clue[1] += sum(phi[1])
            return clue

        clue=[0, 0]
        for space in self.spaces:
            duxed = dux(space)
            clue[0] += duxed[0]
            clue[1] += duxed[1]
        return clue

    def lanceolata(self):
        self.phi=[]

        def dux(scope):
            if scope:
                if 'decision' == scope.type:
                    self.phi.append(scope.capparis())
                for child in scope.getChilds():
                    dux(child)

        for space in self.spaces:
            dux(space)
        
        return self.phi

    def verify(self):
        self.sumphi = [0,0]
        fl = ''
        def dux(scope):
            fl = ''
            if scope:
                if 'decision' == scope.type:
                    phi = scope.capparis()
                    rsum = sum(phi[1])
                    phi = [phi[0], rsum]
                    self.sumphi[0] += phi[0]
                    self.sumphi[1] += phi[1]
                    fl += '['+str(scope.fluo)+']'+str(scope)+' '+u'\u03C6'+str(phi)+ ' { '
                for child in scope.getChilds():
                    dux(child)
                if 'decsision' == scope.type:
                    fl += '} '
            return fl

        for pace in self.spaces:
            fl += dux(pace)
        fl += (u'\u03BE=%s' % self.sumphi)
        return fl

    def cabe(self):
        def dux(scope):
            m=0
            if scope:
                if 'decision' == scope.type:
                    m += scope.conditions()
                for child in scope.getChilds():
                    m += dux(child)
            return m

        m=0
        for pace in self.spaces:
              m += dux(pace)
        return m + 1

    def subPaths(self, scope=None):
        if scope:
            q = 1
            if 'decision' == scope.type:
                q = scope.ors()+1 # scope entrances
            for child in scope.getChilds():
                q = q*self.subPaths(child)
            if 'decision' == scope.type:
                q += scope.ands()+1 # False exits
            return q
        else:
            q = 1
            for space in self.spaces:
                q = q*self.subPaths(space)
            return q
        return 0

    def subPathConjecture(self, scope=None):
        if scope:
            q = 0
            # print('scope %s, or %s, and %s, leaf: %s' % (scope.text, scope.ors(), scope.ands(), scope.isLeaf()))
            if 'decision' == scope.type:
                if scope.isLeaf():
                    q += (scope.conditions()-1)*2+1
                else:
                    q += scope.conditions() * 2
            for child in scope.getChilds():
                q += self.subPathConjecture(child)

            return q
        else:
            q = 0
            for space in self.spaces:
                v = self.subPathConjecture(space)
                q = q+v
            return q
        return 0


if __name__ == '__main__':


    argparser = argparse.ArgumentParser(description='Static code inspection instrument for c-family syntax (C, C++, Java, ECMAScript, C#, ...), it parses decisions of a standard data input stream (stdin) and calculates absolute numbers.')
    argparser.add_argument('-c', action='store_true', help='cyclomatic complexity, condition count, O(n)')
    argparser.add_argument('-f', '--file', type=argparse.FileType('r'), help='read one or more newline separated lines from file')
    argparser.add_argument('-g', action='store_true', help='control flow path conjecture O(2n)')
    argparser.add_argument('-k', action='store_true', help='clue path complexity, regards nested c-family syntax, O(n^2)')
    argparser.add_argument('-p', action='store_true', help='clue fin path')
    argparser.add_argument('-q', action='store_true', help='all sub paths, O(2^n)')
    argparser.add_argument('-v', action='store_true', help='verify clue fin path')
    args = argparser.parse_args()

    data=''
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
        print(clue.lanceolata())
    elif args.q:
        print(clue.subPaths())
    elif args.g:
        print(clue.subPathConjecture())
    elif args.c:
        print(clue.cabe())
    else:
        print(clue.clue())
