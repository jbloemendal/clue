from ahm import CCodeParser
import unittest


class TestCCodeParser(unittest.TestCase):

    # colloc 1
    def test_colloc1_acyc(self):
        ccode = 'if (a>-1) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.acyc())
    def test_colloc1_cabe(self):
        ccode = 'if (a>-1) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.cabe())
    def test_colloc1_uniquePath(self):
        ccode = 'if (a>-1) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.uniquePath())

    # colloc 2
    def test_colloc_2_acyc(self):
        ccode = 'if (b<3 && c>4) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.acyc())
    def test_colloc_2_cabe(self):
        ccode = 'if (b<3 && c>4) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc_2_uniquePath(self):
        ccode = 'if (b<3 && c>4) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.uniquePath())

    # colloc 3
    def test_colloc3_acyc(self):
        ccode = 'if (b<3 || c>4) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.acyc())
    def test_colloc3_cabe(self):
        ccode = 'if (b<3 || c>4) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc3_uniquePath(self):
        ccode = 'if (b<3 || c>4) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.uniquePath())

    # colloc 4
    def test_colloc4_acyc(self):
        ccode = 'if (d>0) { if(e>3){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.acyc())
    def test_colloc4_cabe(self):
        ccode = 'if (d>0) { if(e>3){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc4_uniquePath(self):
        ccode = 'if (d>0) { if(e>3){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.uniquePath())

    # colloc 5
    def test_colloc5_acyc(self):
        ccode = 'if (f>2) {} if(g<6) {} '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.acyc())
    def test_colloc5_cabe(self):
        ccode = 'if (f>2) {} if(g<6) {} '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc5_uniquePath(self):
        ccode = 'if (f>2) {} if(g<6) {} '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.uniquePath())

    # colloc 6
    def test_colloc6_acyc(self):
        ccode = 'if (h>2 && i<3 && j>10) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_colloc6_cabe(self):
        ccode = 'if (h>2 && i<3 && j>10) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc6_uniquePath(self):
        ccode = 'if (h>2 && i<3 && j>10) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.uniquePath()) 

    # colloc 7
    def test_colloc7_acyc(self):
        ccode = 'if (k>8 && i<5) { if (m<11) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_colloc7_cabe(self):
        ccode = 'if (k>8 && i<5) { if (m<11) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc7_uniquePath(self):
        ccode = 'if (k>8 && i<5) { if (m<11) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.uniquePath()) 

    # colloc 8 
    def test_colloc71_acyc(self):
        ccode = 'if (k>8 || i<5) { if (m<11) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_colloc7_cabe(self):
        ccode = 'if (k>8 || i<5) { if (m<11) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc7_uniquePath(self):
        ccode = 'if (k>8 || i<5) { if (m<11) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.uniquePath()) 

    # colloc 9
    def test_colloc9_acyc(self):
        ccode = 'if (n>0) { if (o<3) {} if (p<12){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.acyc()) 
    def test_colloc9_cabe(self):
        ccode = 'if (n>0) { if (o<3) {} if (p<12){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc9_uniquePath(self):
        ccode = 'if (n>0) { if (o<3) {} if (p<12){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.uniquePath()) 

    # colloc 10
    def test_colloc10_acyc(self):
        ccode = 'if (q>2) { if (r<3) { if (s<3){} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.acyc()) 
    def test_colloc10_cabe(self):
        ccode = 'if (q>2) { if (r<3) { if (s<3){} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc10_uniquePath(self):
        ccode = 'if (q>2) { if (r<3) { if (s<3){} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.uniquePath()) 

    # colloc 11 
    def test_colloc11_acyc(self):
        ccode = 'if (t>2) { if (u>10) { } } if (v>4){ } '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.acyc()) 
    def test_colloc11_cabe(self):
        ccode = 'if (t>2) { if (u>10) { } } if (v>4){ } '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc11_uniquePath(self):
        ccode = 'if (t>2) { if (u>10) { } } if (v>4){ } '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.uniquePath()) 

    # colloc 12 
    def test_colloc12_acyc(self):
        ccode = 'if (w>2) { } if (x>5) { } if (y>3){ } '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.acyc()) 
    def test_colloc12_cabe(self):
        ccode = 'if (w>2) { } if (x>5) { } if (y>3){ } '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc12_uniquePath(self):
        ccode = 'if (w>2) { } if (x>5) { } if (y>3){ } '
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(8, parser.uniquePath()) 



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
    def test_43n_uniquePath(self):
        ccode = 'if (a) { if (b){} if(c){} if(d){} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(9, parser.uniquePath()) 

    
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
    def test_41n_uniquePath(self):
        ccode = 'if (a && (b || c)) { if (d) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.uniquePath()) 


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
    def test_52n_uniquePath(self):
        ccode = 'if (a && (b || c)) { if (d) { } if (e) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(10, parser.uniquePath()) 



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
    def test_for_uniquePath(self):
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
    def test_while_uniquePath(self):
        ccode = 'while (i<=9) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.uniquePath())


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

    def test_example_uniquePath(self):
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
        self.assertEqual(7, parser.uniquePath()) 

if __name__ == '__main__':
    unittest.main()
