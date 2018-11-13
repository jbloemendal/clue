import re
from parsimonious.grammar import Grammar

class Decision:
    sor = '||'
    sand = '&&'
    jack = ''
    text = '' 
    level = 0

    def __init__(self, jack, level, text):
        self.jack = jack
        self.level = level
        self.text = text

    def conditions(self):
        return 1+self.text.count(self.sor) + self.text.count(self.sand)

    def rate(self):
        return self.conditions() + self.level*self.conditions()

    def getLevel(self):
        return self.level

    def __repr__(self):
        return "%s %s %s %s (%s)" % (self.level, self.conditions(), self.jack, self.text, self.rate())

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

        m = re.search(r'\s*for\s*\((.*?)\)\s*$', text)
        if m:
            d = Decision('for', level, m.group(1))
            self.decisions.append(d)

        m = re.search(r'\s*while\s*\((.*)\)\s*$', text)
        if m:
            d = Decision('while', level, m.group(1))
            self.decisions.append(d)

    def squigglyL(self, level):
        pattern = re.compile('^([^{}]*){')
        match = pattern.match(self.text)
        if match:
            self.ramify(level, match.group(1))
            self.text = self.text[len(match.group(0)):]
            return True
        return False

    def squigglyR(self, level):
        pattern = re.compile('^([^}]*)}')
        match = pattern.match(self.text)
        if match:
            self.text = self.text[len(match.group(0)):]
            return True
        return False

    def scope(self, level=0):
        if not self.squigglyL(level):
            return False
        while self.scope(level+1):
            pass
        self.squigglyR(level)
        return True

    def complexity(self):
        c=0
        for d in self.decisions:
            c += d.rate()
        return c

    def getDecisions(self):
        return self.decisions


if __name__ == '__main__':
    parser = CCodeParser('if (a && (b || c)) { if (d) { } }')
    parser.parse()

    for d in parser.getDecisions():
        print(d)

    print(parser.complexity())
