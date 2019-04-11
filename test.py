from ahm import CCodeParser
import unittest


class TestCCodeParser(unittest.TestCase):

    # colloc 1
    def test_colloc1_acyc(self):
        ccode = 'if (-1<1) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.acyc())
    def test_colloc1_cabe(self):
        ccode = 'if (-1<l) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.cabe())
    def test_colloc1_subPaths(self):
        ccode = 'if (-1<l) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.subPaths())
    def test_colloc1_subPathsEnclosed(self):
        ccode = 'if (-1<l) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1, parser.subPathsEnclosed())

    # colloc 2
    def test_colloc_2_acyc(self):
        ccode = 'if (3>l && 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1/2, parser.acyc())
    def test_colloc_2_cabe(self):
        ccode = 'if (3>l && 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc_2_subPaths(self):
        ccode = 'if (3>l && 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPaths())
    def test_colloc_2_subPathsEnclosed(self):
        ccode = 'if (3>l && 0<k) { }'
        parser = CCodeParser(ccode)
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPathsEnclosed())


    # colloc 3
    def test_colloc3_acyc(self):
        ccode = 'if (2>l && 7>k && 10>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1/2+1/3, parser.acyc())
    def test_colloc3_cabe(self):
        ccode = 'if (2>l && 7>k && 10>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe())
    def test_colloc3_subPaths(self):
        ccode = 'if (2>l && 7>k && 10>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPaths())
    def test_colloc3_subPathsEnclosed(self):
        ccode = 'if (2>l && 7>k && 10>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPathsEnclosed())

    # colloc 4
    def test_colloc4_acyc(self):
        ccode = 'if (2>l || 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1, parser.acyc())
    def test_colloc4_cabe(self):
        ccode = 'if (2>l || 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc4_subPaths(self):
        ccode = 'if (2>l || 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPaths())
    def test_colloc4_subPathsEnclosed(self):
        ccode = 'if (2>l || 0<k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPathsEnclosed())

    # colloc 5
    def test_colloc5_acyc(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1, parser.acyc())
    def test_colloc5_cabe(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe())
    def test_colloc5_subPaths(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPaths())
    def test_colloc5_subPathsEnclosed(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPathsEnclosed())

    # colloc 6
    def test_colloc6_acyc(self):
        ccode = 'if (0<l && 4>k) { if (11>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1/2+1, parser.acyc()) 
    def test_colloc6_cabe(self):
        ccode = 'if (0<l && 4>k) { if (11>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc6_subPaths(self):
        ccode = 'if (0<l && 4>k) { if (11>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPaths()) 
    def test_colloc6_subPathsEnclosed(self):
        ccode = 'if (0<l && 4>k) { if (11>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPathsEnclosed()) 

    # colloc 7
    def test_colloc7_acyc(self):
        ccode = 'if (2>l && 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1/2+1, parser.acyc()) 
    def test_colloc7_cabe(self):
        ccode = 'if (2>l && 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc7_subPaths(self):
        ccode = 'if (2>l && 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPaths()) 
    def test_colloc7_subPathsEnclosed(self):
        ccode = 'if (2>l && 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPathsEnclosed()) 

    # colloc 8 
    def test_colloc8_acyc(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+2, parser.acyc()) 
    def test_colloc8_cabe(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        parser = CCodeParser(ccode)
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.cabe()) 
    def test_colloc8_subPaths(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        parser = CCodeParser(ccode)
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPaths()) 
    def test_colloc8_subPathsEnclosed(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        parser = CCodeParser(ccode)
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.subPathsEnclosed()) 

    # colloc 9
    def test_colloc9_acyc(self):
        ccode = 'if (2>l || 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1+1, parser.acyc()) 
    def test_colloc9_cabe(self):
        ccode = 'if (2>l || 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc9_subPaths(self):
        ccode = 'if (2>l || 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPaths()) 
    def test_colloc9_subPathsEnclosed(self):
        ccode = 'if (2>l || 0<k || 4>m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPathsEnclosed()) 

    # colloc 10
    def test_colloc10_acyc(self):
        ccode = 'if (2>l) { if (8>k) { if (2<m) {} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1+1, parser.acyc()) 
    def test_colloc10_cabe(self):
        ccode = 'if (2>l) { if (8>k) { if (2<m) {} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc10_subPaths(self):
        ccode = 'if (2>l) { if (8>k) { if (2<m) {} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPaths()) 
    def test_colloc10_subPathsEnclosed(self):
        ccode = 'if (2>l) { if (8>k) { if (2<m) {} } }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPathsEnclosed()) 

    # colloc 11 
    def test_colloc11_acyc(self):
        ccode = 'if (0<l) { if(4>k){} if (8>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1+2, parser.acyc()) 
    def test_colloc11_cabe(self):
        ccode = 'if (0<l) { if(4>k){} if (8>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc11_subPaths(self):
        ccode = 'if (0<l) { if(4>k){} if (8>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(5, parser.subPaths()) 
    def test_colloc11_subPathsEnclosed(self):
        ccode = 'if (0<l) { if(4>k){} if (8>m) {} }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPathsEnclosed()) 

    # colloc 12 
    def test_colloc12_acyc(self):
        ccode = 'if (0<l) { if (8>k) { } } if (2<m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+1+2, parser.acyc()) 
    def test_colloc12_cabe(self):
        ccode = 'if (0<l) { if (8>k) { } } if (2<m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc12_subPaths(self):
        ccode = 'if (0<l) { if (8>k) { } } if (2<m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(6, parser.subPaths()) 
    def test_colloc12_subPathsEnclosed(self):
        ccode = 'if (0<l) { if (8>k) { } } if (2<m) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.subPathsEnclosed()) 

    # colloc 13 
    def test_colloc13_acyc(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8<m) {}'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(1+2+3, parser.acyc()) 
    def test_colloc13_cabe(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8<m) {}'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(4, parser.cabe()) 
    def test_colloc13_subPaths(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8<m) {}'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(8, parser.subPaths()) 
    def test_colloc13_subPathsEnclosed(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8<m) {}'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(3, parser.subPathsEnclosed()) 


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
    def test_for_subPaths(self):
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
    def test_while_subPaths(self):
        ccode = 'while (i<=9) { }'
        parser = CCodeParser(ccode)
        parser.parse()
        self.assertEqual(2, parser.subPaths())


    def test_self1_acyc_equal(self):
        ccode = '{ if (a) { } if (b) { } if (c) { } }'
        parser = CCodeParser(ccode)
        parser.parse()
        parallel = parser.acyc()

        ccode = '{ if (a) { if (b) { if (c) { } } } }'
        parser = CCodeParser(ccode)
        parser.parse()
        orthogonal = parser.acyc()

        self.assertEqual(True, orthogonal < parallel) 

    
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
        self.assertEqual(1+ 1+1/2 +1+1+1, parser.acyc()) #6.5

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

    def test_example_subPaths(self):
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
        self.assertEqual(7, parser.subPaths()) 

if __name__ == '__main__':
    unittest.main()
