import re
from parsimonious.grammar import Grammar

class Scope:
    type = '{}' # class, function (func), flow, encapsulation ({})
    jack = ''
    level = ''
    parent = None

    def __init__(self, type='{}', level=0, jack=''):
        self.type = type
        self.level = level
        self.jack = jack

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __repr__(self):
        return "%s %s" % (self.type, self.jack)


class Decision(Scope):
    sor = '||'
    sand = '&&'
    jack = ''
    text = '' 
    level = 0

    def __init__(self, jack, level, text):
        self.jack = jack
        self.type = 'decision'
        self.level = level
        self.text = text

    def conditions(self):
        return 1+self.text.count(self.sor) + self.text.count(self.sand)

    def scale(self):
        s = self.conditions()
        for c in range(0, self.conditions()):
            s += c + self.level
        return s

    def getLevel(self):
        return self.level

    def __repr__(self):
        return "(%s) %s (%s)" % (self.scale(), self.jack, re.sub(r"[\s\n\t]+", ' ', self.text))

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
class CCodeParser:

    text = ''
    spaces = []

    def __init__(self, text):
        self.text = text
        self.spaces = []

    def parse(self):
        return self.scopes()

    def ramify(self, level, text):
        mif = re.search(r"\s*if\s*\((.*)\)\s*$", text, re.DOTALL)
        mfor = re.search(r'\s*for\s*\((.*?)\)\s*$', text, re.DOTALL)
        mwhile = re.search(r'\s*while\s*\((.*)\)\s*$', text, re.DOTALL)
        mfunction = re.search(r'\s*([a-zA-Z0-9_]+\(.*\))\s*$', text, re.DOTALL)

        if mif:
            d = Decision('if', level, mif.group(1))
            self.spaces.append(d)
            return d
        elif mfor:
            d = Decision('for', level, mfor.group(1))
            self.spaces.append(d)
            return d
        elif mwhile:
            d = Decision('while', level, mwhile.group(1))
            self.spaces.append(d)
            return d

        return Scope()

    def squigglyL(self, level):
        pattern = re.compile('^([^{}]*){')
        match = pattern.match(self.text)
        if match:
            scope = self.ramify(level, match.group(1))
            self.text = self.text[len(match.group(0)):]
            return scope
        return None

    def squigglyR(self):
        pattern = re.compile('^([^}]*)}')
        match = pattern.match(self.text)
        if match:
            self.text = self.text[len(match.group(0)):]
            return True
        return False

    def scopes(self, parent=None, level=0):
        scOpes = []
        s = self.scope(parent, level)
        while s:
            s = self.scope(parent, level)
            scOpes.append(s)
        return scOpes

    def scope(self, parent=None, level=0):
        scOpe = self.squigglyL(level)
        if not scOpe:
            return None

        scOpe.setParent(parent)
        if type(scOpe) is Decision:
            level += 1 + scOpe.conditions()-1

        self.scopes(scOpe, level)

        self.squigglyR()
        return scOpe

    def getScopes(self):
        return self.spaces

    def acyc(self):
        acm=0
        for pace in self.spaces:
            if pace.type == 'decision':
                acm += pace.scale()
        return acm

    def cabe(self):
        m=0
        for pace in self.spaces:
            if pace.type == 'decision':
                m += pace.conditions()
        return m + 1

    def trace(self):
        for pace in self.spaces:
            print(pace, end='')
            scope = pace.getParent()
            while scope:
                print(' \\ ', end='')
                print(scope, end='')
                scope = scope.getParent()
            print()

if __name__ == '__main__':
    code1 = '{ if (a) { } if (b) { } if (c) { } }'
    code2 = '{ if (a && b && c) { if (d) { } } }'
    code3 = '{ if (a) { if (b) { if (c) { if (d) { } } } } }'

    parser = CCodeParser(code3)
    parser.parse()
    parser.trace()
    print(parser.acyc())
