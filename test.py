from acyclic import CCodeParser
import unittest

class TestCCodeParser(unittest.TestCase):

    def test_if_a(self):
        ccode = 'if (a) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.complexity())

    def test_if_ab(self):
        ccode = 'if (a && b) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.complexity())

    def test_if_c(self):
        ccode = 'if (a && (b || c)) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.complexity()) 

    def test_for(self):
        ccode = 'for (int i; i<=9; i++) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.complexity())

    def test_while(self):
        ccode = 'while (i<=9) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.complexity())

    def test_nesting1(self):
        ccode = 'if (a && (b || c)) { if (d) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.complexity()) 

    def test_nesting2(self):
        ccode = 'if (a && (b || c)) { if (d) { } if (e) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(7, parser.complexity()) 

    def test_nesting3(self):
        ccode = '{ if (a) { } if (b) { } if (c) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        non = parser.complexity()

        ccode = '{ if (a) { if (b) { if (c) { } } } }'
        parser = CCodeParser(ccode)
        parser.parse()
        nested = parser.complexity()

        self.assertEqual(True, nested > non) 

if __name__ == '__main__':
    unittest.main()
