from ksi import Ksi
import unittest


class TestKsi(unittest.TestCase):

    def test_ksi0(self):
        ksi = Ksi('f(a) {}')
        ksi.parse()
        self.assertEqual(0, ksi.ksi())

    def test_ksi0(self):
        ksi = Ksi('if(a)')
        ksi.parse()
        self.assertEqual(0, ksi.ksi())

    def test_ksi0(self):
        ksi = Ksi('if(a {}')
        ksi.parse()
        self.assertEqual(0, ksi.ksi())

    def test_ksi0(self):
        ksi = Ksi('if(a) }')
        ksi.parse()
        self.assertEqual(0, ksi.ksi())

    def test_ksi1(self):
        ksi = Ksi('if(a)')
        ksi.parse()
        self.assertEqual(1, ksi.ksi())

    def test_ksi1(self):
        ksi = Ksi('if(a){}')
        ksi.parse()
        self.assertEqual(1, ksi.ksi())

    def test_ksi2(self):
        ksi = Ksi('if(a && b){}')
        ksi.parse()
        self.assertEqual(1+1/2, ksi.ksi())
        
    def test_ksi3(self):
        ksi = Ksi('if(a || b){}')
        ksi.parse()
        self.assertEqual(1+1, ksi.ksi())

    def test_ksi4(self):
        ksi = Ksi('if(a){ if (b) {}}')
        ksi.parse()
        self.assertEqual(1+1, ksi.ksi())

    def test_ksi5(self):
        ksi = Ksi('if(a){ if (b) {}} if (c) {}')
        ksi.parse()
        self.assertEqual(1+1+2, ksi.ksi())

    def test_ksi6(self):
        ksi = Ksi('for(int i=0; i<10; i++) {}')
        ksi.parse()
        self.assertEqual(1, ksi.ksi())

    def test_ksi7(self):
        ksi = Ksi('while (i<10) {}')
        ksi.parse()
        self.assertEqual(1, ksi.ksi())

    def test_ksi8(self):
        ksi = Ksi('if (a) {}')
        ksi.parse()
        self.assertEqual(1, ksi.subPathConjecture())

    def test_ksi9(self):
        ksi = Ksi('if (a) { if (b) {}}')
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())

    def test_ksi10(self):
        ksi = Ksi('if (a) {}')
        ksi.parse()
        self.assertEqual(2, ksi.subPaths())

    def test_ksi11(self):
        ksi = Ksi('if (a) { if (b) {} }')
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())

    def test_ksi12(self):
        ksi = Ksi('if (a) { }')
        ksi.parse()
        self.assertEqual(1, ksi.verify())

    def test_ksi13(self):
        ksi = Ksi('if (a) { if (b) {} }')
        ksi.parse()
        self.assertEqual(2, ksi.verify())

    # colloc 1
    def test_colloc1_xi(self):
        code = 'if (-1<1) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1, ksi.ksi())
    def test_colloc1_cabe(self):
        code = 'if (-1<l) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())
    def test_colloc1_subPaths(self):
        code = 'if (-1<l) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.subPaths())
    def test_colloc1_subPathConjecture(self):
        code = 'if (-1<l) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1, ksi.subPathConjecture())

    # colloc 2
    def test_colloc_2_xi(self):
        code = 'if (3>l && 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1/2, ksi.ksi())
    def test_colloc_2_cabe(self):
        code = 'if (3>l && 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.cabe())
    def test_colloc_2_subPaths(self):
        code = 'if (3>l && 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())
    def test_colloc_2_subPathConjecture(self):
        code = 'if (3>l && 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())


    # colloc 3
    def test_colloc3_xi(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1/2+1/3, ksi.ksi())
    def test_colloc3_cabe(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe())
    def test_colloc3_subPaths(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths())
    def test_colloc3_subPathConjecture(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture())

    # colloc 4
    def test_colloc4_xi(self):
        code = 'if (2>l || 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1, ksi.ksi())
    def test_colloc4_cabe(self):
        code = 'if (2>l || 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.cabe())
    def test_colloc4_subPaths(self):
        code = 'if (2>l || 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())
    def test_colloc4_subPathConjecture(self):
        code = 'if (2>l || 0<k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())

    # colloc 5
    def test_colloc5_xi(self):
        code = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1, ksi.ksi())
    def test_colloc5_cabe(self):
        code = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.cabe())
    def test_colloc5_subPaths(self):
        code = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPaths())
    def test_colloc5_subPathConjecture(self):
        code = 'if (0<l) { if (2>k) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture())

    # colloc 6
    def test_colloc6_xi(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1/2+1, ksi.ksi()) 
    def test_colloc6_cabe(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc6_subPaths(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc6_subPathConjecture(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 7
    def test_colloc7_xi(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1/2+1, ksi.ksi()) 
    def test_colloc7_cabe(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc7_subPaths(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc7_subPathConjecture(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 8
    def test_colloc8_xi(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1+1/2, ksi.ksi()) 
    def test_colloc8_cabe(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc8_subPaths(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc8_subPathConjecture(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 9 
    def test_colloc9_xi(self):
        code = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+2, ksi.ksi()) 
    def test_colloc9_cabe(self):
        code = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.cabe()) 
    def test_colloc9_subPaths(self):
        code = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc9_subPathConjecture(self):
        code = 'if (2>l) {} if (8>k) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.subPathConjecture()) 

    # colloc 10
    def test_colloc10_xi(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1+1, ksi.ksi()) 
    def test_colloc10_cabe(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc10_subPaths(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc10_subPathConjecture(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 11
    def test_colloc11_xi(self):
        code = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1+1, ksi.ksi()) 
    def test_colloc11_cabe(self):
        code = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc11_subPaths(self):
        code = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPaths()) 
    def test_colloc11_subPathConjecture(self):
        code = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPathConjecture()) 

    # colloc 12 
    def test_colloc12_xi(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1+2, ksi.ksi()) 
    def test_colloc12_cabe(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc12_subPaths(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(5, ksi.subPaths()) 
    def test_colloc12_subPathConjecture(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 

    # colloc 13 
    def test_colloc13_xi(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+1+2, ksi.ksi()) 
    def test_colloc13_cabe(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc13_subPaths(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(6, ksi.subPaths()) 
    def test_colloc13_subPathConjecture(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 

    # colloc 14 
    def test_colloc14_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+2+1/2, ksi.ksi()) 
    def test_colloc14_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc14_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(6, ksi.subPaths()) 
    def test_colloc14_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 

    # colloc 15 
    def test_colloc15_xi(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+2+1, ksi.ksi()) 
    def test_colloc15_cabe(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc15_subPaths(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(6, ksi.subPaths()) 
    def test_colloc15_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.subPathConjecture()) 


    # colloc 16 
    def test_colloc16_xi(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1+2+3, ksi.ksi()) 
    def test_colloc16_cabe(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(4, ksi.cabe()) 
    def test_colloc16_subPaths(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(8, ksi.subPaths()) 
    def test_colloc16_subPathConjecture(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(3, ksi.subPathConjecture()) 

    # (colloc 17)
    def test_colloc17_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1 + 2+1/2 + 3+1, ksi.ksi()) 
    def test_colloc17_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(6, ksi.cabe()) 
    def test_colloc17_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(18, ksi.subPaths()) 
    def test_colloc17_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(7, ksi.subPathConjecture()) 

    # (colloc 18)
    def test_colloc18_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1 + 2+1/2 + 3+1/2, ksi.ksi()) 
    def test_colloc18_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(6, ksi.cabe()) 
    def test_colloc18_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(18, ksi.subPaths()) 
    def test_colloc18_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(7, ksi.subPathConjecture()) 

    def test_for_xi(self):
        code = 'for (int i; i<=9; i++) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1, ksi.ksi())
    def test_for_babe(self):
        code = 'for (int i; i<=9; i++) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())
    def test_for_subPaths(self):
        code = 'for (int i; i<=9; i++) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())


    def test_while_xi(self):
        code = 'while (i<=9) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(1, ksi.ksi())
    def test_while_cabe(self):
        code = 'while (i<=9) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.cabe())
    def test_while_subPaths(self):
        code = 'while (i<=9) { }'
        ksi = Ksi(code)
        ksi.parse()
        self.assertEqual(2, ksi.subPaths())


    def test_self1_xi_equal(self):
        code = '{ if (a) { } if (b) { } if (c) { } }'
        ksi = Ksi(code)
        ksi.parse()
        parallel = ksi.ksi()

        code = '{ if (a) { if (b) { if (c) { } } } }'
        ksi = Ksi(code)
        ksi.parse()
        orthogonal = ksi.ksi()

        self.assertEqual(True, orthogonal < parallel) 


if __name__ == '__main__':
    unittest.main()
