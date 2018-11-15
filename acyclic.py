import re
from parsimonious.grammar import Grammar

class Scope:
    type = '{}' # class, function (func), flow, encapsulation ({})
    parent = None

    def __init__(self, type='{}'):
        self.type = type

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __repr__(self):
        return "%s" % (self.type)


class Decision(Scope):
    sor = '||'
    sand = '&&'
    jack = ''
    text = '' 
    level = 0

    def __init__(self, jack, level, text):
        self.jack = jack
        self.type = jack
        self.level = level
        self.text = text

    def conditions(self):
        return 1+self.text.count(self.sor) + self.text.count(self.sand)

    def rate(self):
        rate = self.conditions()
        for d in range(0, self.conditions()):
            rate += d + self.level
        return rate

    def getLevel(self):
        return self.level

    def __repr__(self):
        return "(%s) %s (%s)" % (self.rate(), self.jack, self.text)

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
    decisions = []

    def __init__(self, text):
        self.text = text
        self.decisions = []

    def parse(self):
        return self.scope()

    def ramify(self, level, text):
        m = re.search(r"\s*if\s*\((.*)\)\s*$", text)
        if m:
            d = Decision('if', level, m.group(1))
            self.decisions.append(d)
            return d

        m = re.search(r'\s*for\s*\((.*?)\)\s*$', text)
        if m:
            d = Decision('for', level, m.group(1))
            self.decisions.append(d)
            return d

        m = re.search(r'\s*while\s*\((.*)\)\s*$', text)
        if m:
            d = Decision('while', level, m.group(1))
            self.decisions.append(d)
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

    def scope(self, parent=None, level=0):
        scOpe = self.squigglyL(level)
        if not scOpe:
            return None
        scOpe.setParent(parent)
        if type(scOpe) is Decision:
            level += 1 + scOpe.conditions()-1
        while self.scope(scOpe, level):
            pass
        self.squigglyR()
        return scOpe

    def complexity(self):
        c=0
        for d in self.decisions:
            c += d.rate()
        return c

    def getDecisions(self):
        return self.decisions


if __name__ == '__main__':
    code1 = '{ if (a) { } if (b) { } if (c) { } }'
    code2 = '{ if (a && b && c) { if (d) { } } }'
    code3 = '{ if (a) { if (b) { if (c) { if (d) { } } } } }'

    parser = CCodeParser(code3)
    parser.parse()

    for d in parser.getDecisions():
        print(d, end='')
        scope = d.getParent()
        while scope:
            print(', ', end='')
            print(scope, end='')
            scope = scope.getParent()
        print()

    print(parser.complexity())
