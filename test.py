from ksi import Ksi
import unittest


class TestKsi(unittest.TestCase):

    # colloc 1
    def test_colloc1_xi(self):
        ccode = 'if (-1<1) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1, ksi.ksi())
    def test_colloc1_cabe(self):
        ccode = 'if (-1<l) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())
    def test_colloc1_subPaths(self):
        ccode = 'if (-1<l) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.subPaths())
    def test_colloc1_subPathConjecture(self):
        ccode = 'if (-1<l) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1, ksi.subPathConjecture())

    # colloc 2
    def test_colloc_2_xi(self):
        ccode = 'if (3>l && 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1/2, ksi.ksi())
    def test_colloc_2_cabe(self):
        ccode = 'if (3>l && 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.cabe())
    def test_colloc_2_subPaths(self):
        ccode = 'if (3>l && 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())
    def test_colloc_2_subPathConjecture(self):
        ccode = 'if (3>l && 0<k) { }'
        ksi = Ksi(ccode)
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())


    # colloc 3
    def test_colloc3_xi(self):
        ccode = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1/2+1/3, ksi.ksi())
    def test_colloc3_cabe(self):
        ccode = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe())
    def test_colloc3_subPaths(self):
        ccode = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths())
    def test_colloc3_subPathConjecture(self):
        ccode = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture())

    # colloc 4
    def test_colloc4_xi(self):
        ccode = 'if (2>l || 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1, ksi.ksi())
    def test_colloc4_cabe(self):
        ccode = 'if (2>l || 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.cabe())
    def test_colloc4_subPaths(self):
        ccode = 'if (2>l || 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())
    def test_colloc4_subPathConjecture(self):
        ccode = 'if (2>l || 0<k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())

    # colloc 5
    def test_colloc5_xi(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1, ksi.ksi())
    def test_colloc5_cabe(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.cabe())
    def test_colloc5_subPaths(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())
    def test_colloc5_subPathConjecture(self):
        ccode = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())

    # colloc 6
    def test_colloc6_xi(self):
        ccode = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1/2+1, ksi.ksi()) 
    def test_colloc6_cabe(self):
        ccode = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc6_subPaths(self):
        ccode = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc6_subPathConjecture(self):
        ccode = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 7
    def test_colloc7_xi(self):
        ccode = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1/2+1, ksi.ksi()) 
    def test_colloc7_cabe(self):
        ccode = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc7_subPaths(self):
        ccode = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc7_subPathConjecture(self):
        ccode = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 8
    def test_colloc8_xi(self):
        ccode = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1+1/2, ksi.ksi()) 
    def test_colloc8_cabe(self):
        ccode = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc8_subPaths(self):
        ccode = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc8_subPathConjecture(self):
        ccode = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 9 
    def test_colloc9_xi(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+2, ksi.ksi()) 
    def test_colloc9_cabe(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(ccode)
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.cabe()) 
    def test_colloc9_subPaths(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(ccode)
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc9_subPathConjecture(self):
        ccode = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(ccode)
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.subPathConjecture()) 

    # colloc 10
    def test_colloc10_xi(self):
        ccode = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1+1, ksi.ksi()) 
    def test_colloc10_cabe(self):
        ccode = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc10_subPaths(self):
        ccode = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc10_subPathConjecture(self):
        ccode = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 11
    def test_colloc11_xi(self):
        ccode = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1+1, ksi.ksi()) 
    def test_colloc11_cabe(self):
        ccode = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc11_subPaths(self):
        ccode = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc11_subPathConjecture(self):
        ccode = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 12 
    def test_colloc12_xi(self):
        ccode = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1+2, ksi.ksi()) 
    def test_colloc12_cabe(self):
        ccode = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc12_subPaths(self):
        ccode = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(5, ksi.subPaths()) 
    def test_colloc12_subPathConjecture(self):
        ccode = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 

    # colloc 13 
    def test_colloc13_xi(self):
        ccode = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+1+2, ksi.ksi()) 
    def test_colloc13_cabe(self):
        ccode = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc13_subPaths(self):
        ccode = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(6, ksi.subPaths()) 
    def test_colloc13_subPathConjecture(self):
        ccode = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 

    # colloc 14 
    def test_colloc14_xi(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+2+1/2, ksi.ksi()) 
    def test_colloc14_cabe(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc14_subPaths(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(6, ksi.subPaths()) 
    def test_colloc14_subPathConjecture(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 

    # colloc 15 
    def test_colloc15_xi(self):
        ccode = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+2+1, ksi.ksi()) 
    def test_colloc15_cabe(self):
        ccode = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc15_subPaths(self):
        ccode = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(6, ksi.subPaths()) 
    def test_colloc15_subPathConjecture(self):
        ccode = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 


    # colloc 16 
    def test_colloc16_xi(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1+2+3, ksi.ksi()) 
    def test_colloc16_cabe(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc16_subPaths(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(8, ksi.subPaths()) 
    def test_colloc16_subPathConjecture(self):
        ccode = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture()) 

    # (colloc 17)
    def test_colloc17_xi(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1 + 2+1/2 + 3+1, ksi.ksi()) 
    def test_colloc17_cabe(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(6, ksi.cabe()) 
    def test_colloc17_subPaths(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(18, ksi.subPaths()) 
    def test_colloc17_subPathConjecture(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(7, ksi.subPathConjecture()) 

    # (colloc 18)
    def test_colloc18_xi(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1 + 2+1/2 + 3+1/2, ksi.ksi()) 
    def test_colloc18_cabe(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(6, ksi.cabe()) 
    def test_colloc18_subPaths(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(18, ksi.subPaths()) 
    def test_colloc18_subPathConjecture(self):
        ccode = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(7, ksi.subPathConjecture()) 

    def test_for_xi(self):
        ccode = 'for (int i; i<=9; i++) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1, ksi.ksi())
    def test_for_babe(self):
        ccode = 'for (int i; i<=9; i++) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())
    def test_for_subPaths(self):
        ccode = 'for (int i; i<=9; i++) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())


    def test_while_xi(self):
        ccode = 'while (i<=9) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(1, ksi.ksi())
    def test_while_cabe(self):
        ccode = 'while (i<=9) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())
    def test_while_subPaths(self):
        ccode = 'while (i<=9) { }'
        ksi = Ksi(ccode)
        ksi.parse()
        self.assertEqual(2, ksi.subPaths())


    def test_self1_xi_equal(self):
        ccode = '{ if (a) { } if (b) { } if (c) { } }'
        ksi = Ksi(ccode)
        ksi.parse()
        parallel = ksi.ksi()

        ccode = '{ if (a) { if (b) { if (c) { } } } }'
        ksi = Ksi(ccode)
        ksi.parse()
        orthogonal = ksi.ksi()

        self.assertEqual(True, orthogonal < parallel) 

    
    def test_example_xi(self):
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
        ksi = Ksi(ccode)
        scopes = ksi.parse()
        self.assertEqual(1+ 1+1/2 +1+1+1, ksi.ksi()) #6.5

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
        ksi = Ksi(ccode)
        scopes = ksi.parse()
        self.assertEqual(7, ksi.cabe()) 

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
        ksi = Ksi(ccode)
        scopes = ksi.parse()
        self.assertEqual(7, ksi.subPaths()) 

if __name__ == '__main__':
    unittest.main()
