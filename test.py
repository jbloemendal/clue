from ahm import CCodeParser
import unittest


class TestCCodeParser(unittest.TestCase):

    def test_if_1_acyc(self):
        ccode = 'if (a) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.acyc())
    def test_if_1_cabe(self):
        ccode = 'if (a) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.cabe())
    def test_if_1_paths(self):
        ccode = 'if (a) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.paths())


    def test_if_2_acyc(self):
        ccode = 'if (a && b) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.acyc())
    def test_if_2_cabe(self):
        ccode = 'if (a && b) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_if_2_paths(self):
        ccode = 'if (a && b) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())

    def test_if_21n_acyc(self):
        ccode = 'if (a) { if(b){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.acyc())
    def test_if_21n_cabe(self):
        ccode = 'if (a) { if(b){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_if_21n_paths(self):
        ccode = 'if (a) { if(b){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())


    def test_if_3_acyc(self):
        ccode = 'if (a && (b || c)) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_if_3_cabe(self):
        ccode = 'if (a && (b || c)) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_if_3_paths(self):
        ccode = 'if (a && (b || c)) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.paths()) 


    def test_if_31n_acyc(self):
        ccode = 'if (a && b) { if(c){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_if_31n_cabe(self):
        ccode = 'if (a && b) { if(c){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_if_31n_path(self):
        ccode = 'if (a && b) { if(c){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.paths()) 

    '''
    mc cabe doesn't evaluate nested structures
    acycl. decreases due to decrease of dependent decision memory (visual perception)
    the amount of paths through the program increases
    '''
    def test_32n_cycl(self):
        ccode = 'if (a) { if(b){} if(c){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.acyc()) 
    def test_32n_cabe(self):
        ccode = 'if (a) { if(b){} if(c){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_32n_paths(self):
        ccode = 'if (a) { if(b){} if(c){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.paths()) 


    def test_nesting31n1n_cycl(self):
        ccode = 'if (a) { if(b){ if(c){} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_nesting31n1n_cabe(self):
        ccode = 'if (a) { if(b){ if(c){} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_nesting31n1n_paths(self):
        ccode = 'if (a) { if(b){ if(c){} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.paths()) 


    def test_43n_acyc(self):
        ccode = 'if (a) { if(b){} if(c){} if(d){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(7, parser.acyc()) 
    def test_43n_cabe(self):
        ccode = 'if (a) { if(b){} if(c){} if(d){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.cabe()) 
    def test_43n_paths(self):
        ccode = 'if (a) { if (b){} if(c){} if(d){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(9, parser.paths()) 

    
    def test_41n_acyc(self):
        ccode = 'if (a && (b || c)) { if (d) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(10, parser.acyc()) 
    def test_41n_cabe(self):
        ccode = 'if (a && (b || c)) { if (d) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.cabe()) 
    def test_41n_paths(self):
        ccode = 'if (a && (b || c)) { if (d) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.paths()) 


    def test_52n_acyc(self):
        ccode = 'if (a && (b || c)) { if (d) { } if (e) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(14, parser.acyc()) 
    def test_52n_cabe(self):
        ccode = 'if (a && (b || c)) { if (d) { } if (e) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.cabe()) 
    def test_52n_paths(self):
        ccode = 'if (a && (b || c)) { if (d) { } if (e) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(10, parser.paths()) 



    def test_for_acyc(self):
        ccode = 'for (int i; i<=9; i++) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.acyc())
    def test_for_babe(self):
        ccode = 'for (int i; i<=9; i++) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.cabe())
    def test_for_paths(self):
        ccode = 'for (int i; i<=9; i++) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.cabe())


    def test_while_acyc(self):
        ccode = 'while (i<=9) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.acyc())
    def test_while_cabe(self):
        ccode = 'while (i<=9) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.cabe())
    def test_while_paths(self):
        ccode = 'while (i<=9) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.paths())


    def test_folding_acyc(self):
        ccode = '{ if (a && b && c) { if (d) { } } }'
        parser = CCodeParser(ccode)
        parser.parse()
        folded = parser.acyc()

        ccode = '{ if (a) { if (b) { if (c) { if (d) { } } } } }'
        parser = CCodeParser(ccode)
        parser.parse()
        nested = parser.acyc()

        self.assertEqual(nested, folded) 

    def test_folding_paths(self):
        ccode = '{ if (a && b && c) { if (d) { } } }' # 5
        parser = CCodeParser(ccode)
        parser.parse()
        folded = parser.paths()

        ccode = '{ if (a) { if (b) { if (c) { if (d) { } } } } }' #5
        parser = CCodeParser(ccode)
        parser.parse()
        nested = parser.paths()

        self.assertEqual(nested, folded) 

    def test_scopes(self):
        ccode = '{if (a) {}} {if (b) {}}'
        parser = CCodeParser(ccode)
        parser.parse()
        n = parser.acyc()
        self.assertEqual(2, n) 

    def test_scopes2(self):
        ccode = '{if (a) {}} {if (b) {}}'
        parser = CCodeParser(ccode)
        scopes = parser.parse()
        n = parser.acyc()
        self.assertEqual(2, len(scopes)) 

    def test_nesting3_acyc_equal(self):
        ccode = '{ if (a) { } if (b) { } if (c) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        non = parser.acyc()

        ccode = '{ if (a) { if (b) { if (c) { } } } }'
        parser = CCodeParser(ccode)
        parser.parse()
        nested = parser.acyc()

        self.assertEqual(True, nested > non) 

    def test_nesting3_compare_acyc_cabe(self):
        ccode = '{ if (a) { if (b) { if (c) { } } } }'
        parser = CCodeParser(ccode)
        parser.parse()

        self.assertEqual(True, parser.acyc() > parser.cabe()) 
    
    def test_example_acyc(self):
        ccode = '''
        int size = image.length();
        StringBuilder buf = new StringBuilder(size);
        for (int i = 0; i < size; i++) {
          char c = image.charAt(i);
          if (c == '\\' && i + 1 < size) {
            char c1 = image.charAt(i + 1);
            if (c1 == '\\'
                || c1 == '"'
                || c1 == '\'') {
                c = c1;
                i++;
            }
          }
          buf.append(c);
        }
        '''
        parser = CCodeParser(ccode)
        scopes = parser.parse()
        self.assertEqual(21, parser.acyc()) 

    def test_example_cabe(self):
        ccode = '''
        int size = image.length();
        StringBuilder buf = new StringBuilder(size);
        for (int i = 0; i < size; i++) {
          char c = image.charAt(i);
          if (c == '\\' && i + 1 < size) {
            char c1 = image.charAt(i + 1);
            if (c1 == '\\'
                || c1 == '"'
                || c1 == '\'') {
                c = c1;
                i++;
            }
          }
          buf.append(c);
        }
        '''
        parser = CCodeParser(ccode)
        scopes = parser.parse()
        self.assertEqual(7, parser.cabe()) 

    def test_example_paths(self):
        ccode = '''
        int size = image.length();
        StringBuilder buf = new StringBuilder(size);
        for (int i = 0; i < size; i++) {
          char c = image.charAt(i);
          if (c == '\\' && i + 1 < size) {
            char c1 = image.charAt(i + 1);
            if (c1 == '\\'
                || c1 == '"'
                || c1 == '\'') {
                c = c1;
                i++;
            }
          }
          buf.append(c);
        }
        '''
        parser = CCodeParser(ccode)
        scopes = parser.parse()
        self.assertEqual(9, parser.paths()) 

if __name__ == '__main__':
    unittest.main()
