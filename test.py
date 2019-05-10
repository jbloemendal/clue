from kso import Kso
from fractions import Fraction
import unittest


class TestKso(unittest.TestCase):

    def test_kso0(self):
        kso = Kso('f(a) {}')
        kso.parse()
        self.assertEqual([0, 0], kso.kso())

    def test_kso0(self):
        kso = Kso('if(a)')
        kso.parse()
        self.assertEqual([0, 0], kso.kso())

    def test_kso0(self):
        kso = Kso('if(a {}')
        kso.parse()
        self.assertEqual(0, kso.kso())

    def test_kso0(self):
        kso = Kso('if(a) }')
        kso.parse()
        self.assertEqual([0, 0], kso.kso())

    def test_kso1(self):
        kso = Kso('if(a)')
        kso.parse()
        self.assertEqual([1, 0], kso.kso())

    def test_kso1(self):
        kso = Kso('if(a){}')
        kso.parse()
        self.assertEqual([1, 0], kso.kso())

    def test_kso2(self):
        kso = Kso('if(a && b){}')
        kso.parse()
        self.assertEqual([1, 1/2], kso.kso())
        
    def test_kso3(self):
        kso = Kso('if(a || b){}')
        kso.parse()
        self.assertEqual([1, Fraction(1,1)], kso.kso())

    def test_kso4(self):
        kso = Kso('if(a){ if (b) {}}')
        kso.parse()
        self.assertEqual([2, 0], kso.kso())

    def test_kso5(self):
        kso = Kso('if(a){ if (b) {}} if (c) {}')
        kso.parse()
        self.assertEqual([4, 0], kso.kso())

    def test_kso6(self):
        kso = Kso('for(int i=0; i<10; i++) {}')
        kso.parse()
        self.assertEqual([1, 0], kso.kso())

    def test_kso7(self):
        kso = Kso('while (i<10) {}')
        kso.parse()
        self.assertEqual([1, 0], kso.kso())

    def test_kso8(self):
        kso = Kso('if (a) {}')
        kso.parse()
        self.assertEqual(1, kso.subPathConjecture())

    def test_kso9(self):
        kso = Kso('if (a) { if (b) {}}')
        kso.parse()
        self.assertEqual(3, kso.subPathConjecture())

    def test_kso10(self):
        kso = Kso('if (a) {}')
        kso.parse()
        self.assertEqual(2, kso.subPaths())

    def test_kso11(self):
        kso = Kso('if (a) { if (b) {} }')
        kso.parse()
        self.assertEqual(3, kso.subPaths())


    ''' post '''
    def test_self1_xi_post(self):
        code = '{ if (a) { } if (b) { } if (c) { } }'
        kso = Kso(code)
        kso.parse()
        parallel = kso.kso()

        code = '{ if (a) { if (b) { if (c) { } } } }'
        kso = Kso(code)
        kso.parse()
        orthogonal = kso.kso()

        self.assertEqual(True, orthogonal[0] < parallel[0]) 

    # colloc 1
    def test_colloc1_xi(self):
        code = 'if (-1<1) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, 0], kso.kso())
    def test_colloc1_cabe(self):
        code = 'if (-1<l) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.cabe())
    def test_colloc1_subPaths(self):
        code = 'if (-1<l) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.subPaths())
    def test_colloc1_subPathConjecture(self):
        code = 'if (-1<l) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(1, kso.subPathConjecture())

    # colloc 2
    def test_colloc_2_xi(self):
        code = 'if (3>l && 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, 1/2], kso.kso())
    def test_colloc_2_cabe(self):
        code = 'if (3>l && 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.cabe())
    def test_colloc_2_subPaths(self):
        code = 'if (3>l && 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPaths())
    def test_colloc_2_subPathConjecture(self):
        code = 'if (3>l && 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPathConjecture())


    # colloc 3
    def test_colloc3_xi(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, Fraction(1,2)+Fraction(1,4)], kso.kso())
    def test_colloc3_cabe(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe())
    def test_colloc3_subPaths(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths())
    def test_colloc3_subPathConjecture(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPathConjecture())

    # colloc 4
    def test_colloc4_xi(self):
        code = 'if (2>l || 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, Fraction(1,1)], kso.kso())
    def test_colloc4_cabe(self):
        code = 'if (2>l || 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.cabe())
    def test_colloc4_subPaths(self):
        code = 'if (2>l || 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPaths())
    def test_colloc4_subPathConjecture(self):
        code = 'if (2>l || 0<k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPathConjecture())

    # colloc 5
    def test_colloc5_xi(self):
        code = 'if (0<l) { if (2>k) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([2, 0], kso.kso())
    def test_colloc5_cabe(self):
        code = 'if (0<l) { if (2>k) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.cabe())
    def test_colloc5_subPaths(self):
        code = 'if (0<l) { if (2>k) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPaths())
    def test_colloc5_subPathConjecture(self):
        code = 'if (0<l) { if (2>k) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPathConjecture())

    # colloc 6
    def test_colloc6_xi(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([2, 1/2], kso.kso()) 
    def test_colloc6_cabe(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc6_subPaths(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths()) 
    def test_colloc6_subPathConjecture(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPathConjecture()) 

    # colloc 7
    def test_colloc7_xi(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, Fraction(2,2) + Fraction(2,3)], kso.kso()) 
    def test_colloc7_cabe(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc7_subPaths(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths()) 
    def test_colloc7_subPathConjecture(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPathConjecture()) 

    # colloc 8
    def test_colloc8_xi(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, Fraction(2,1) + Fraction(2,4)], kso.kso()) 
    def test_colloc8_cabe(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc8_subPaths(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths()) 
    def test_colloc8_subPathConjecture(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPathConjecture()) 

    # colloc 9 
    def test_colloc9_xi(self):
        code = 'if (2>l) {} if (8>k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([3, 0], kso.kso()) 
    def test_colloc9_cabe(self):
        code = 'if (2>l) {} if (8>k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.cabe()) 
    def test_colloc9_subPaths(self):
        code = 'if (2>l) {} if (8>k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths()) 
    def test_colloc9_subPathConjecture(self):
        code = 'if (2>l) {} if (8>k) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.subPathConjecture()) 

    # colloc 10
    def test_colloc10_xi(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, Fraction(1,1)+Fraction(1,3)], kso.kso()) 
    def test_colloc10_cabe(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc10_subPaths(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths()) 
    def test_colloc10_subPathConjecture(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPathConjecture()) 

    # colloc 11
    def test_colloc11_xi(self):
        code = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([3, 0], kso.kso()) 
    def test_colloc11_cabe(self):
        code = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc11_subPaths(self):
        code = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPaths()) 
    def test_colloc11_subPathConjecture(self):
        code = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPathConjecture()) 

    # colloc 12 
    def test_colloc12_xi(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([4, 0], kso.kso()) 
    def test_colloc12_cabe(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc12_subPaths(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(5, kso.subPaths()) 
    def test_colloc12_subPathConjecture(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPathConjecture()) 

    # colloc 13 
    def test_colloc13_xi(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([4, 0], kso.kso()) 
    def test_colloc13_cabe(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc13_subPaths(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(6, kso.subPaths()) 
    def test_colloc13_subPathConjecture(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPathConjecture()) 

    # colloc 14 
    def test_colloc14_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([3, 1/2], kso.kso()) 
    def test_colloc14_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc14_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(6, kso.subPaths()) 
    def test_colloc14_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPathConjecture()) 

    # colloc 15 
    def test_colloc15_xi(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([4, 0], kso.kso()) 
    def test_colloc15_cabe(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc15_subPaths(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(6, kso.subPaths()) 
    def test_colloc15_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.subPathConjecture()) 


    # colloc 16 
    def test_colloc16_xi(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([6, 0], kso.kso()) 
    def test_colloc16_cabe(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(4, kso.cabe()) 
    def test_colloc16_subPaths(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(8, kso.subPaths()) 
    def test_colloc16_subPathConjecture(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(3, kso.subPathConjecture()) 

    # (colloc 17)
    def test_colloc17_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([6, Fraction(1,2)+Fraction(1,1)], kso.kso()) 
    def test_colloc17_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(6, kso.cabe()) 
    def test_colloc17_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(18, kso.subPaths()) 
    def test_colloc17_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(7, kso.subPathConjecture()) 

    # (colloc 18)
    def test_colloc18_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([6, 1/2+1/2], kso.kso()) 
    def test_colloc18_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(6, kso.cabe()) 
    def test_colloc18_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(18, kso.subPaths()) 
    def test_colloc18_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(7, kso.subPathConjecture()) 

    def test_for_xi(self):
        code = 'for (int i; i<=9; i++) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, 0], kso.kso())
    def test_for_babe(self):
        code = 'for (int i; i<=9; i++) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.cabe())
    def test_for_subPaths(self):
        code = 'for (int i; i<=9; i++) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.cabe())

    def test_while_xi(self):
        code = 'while (i<=9) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([1, 0], kso.kso())
    def test_while_cabe(self):
        code = 'while (i<=9) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.cabe())
    def test_while_subPaths(self):
        code = 'while (i<=9) { }'
        kso = Kso(code)
        kso.parse()
        self.assertEqual(2, kso.subPaths())

    def test_ksopath_1(self):
        code = 'if (a) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([[1, [0]]], kso.ksopath())

    def test_ksopath_2(self):
        code = 'if (a && b) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([[1, [0.5]]], kso.ksopath())

    def test_ksopath_3(self):
        code = 'if (a || b) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([[1, [Fraction(1, 1)]]], kso.ksopath())

    def test_ksopath_4(self):
        code = 'if (a) { if (b) {}} if (c) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([[1,[0]], [1, [0]], [2, [0]]], kso.ksopath())

    def test_ksopath_5(self):
        code = 'if (a && b || c && d) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([[1, [Fraction(2,4), Fraction(3,1), Fraction(2,4)]]], kso.ksopath()) 

    def test_ksopath6(self):
        code = 'if (a) { if (b) {} } if (c && c1) {} if (d || d1) {} if (e) {}'
        kso = Kso(code)
        kso.parse()
        self.assertEqual([[1, [0]], [1, [0]], [2, [Fraction(1,2)]], [3, [Fraction(1,1)]], [4, [0]]], kso.ksopath())

if __name__ == '__main__':
    unittest.main()
