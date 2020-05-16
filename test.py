from clue import Clue
from fractions import Fraction
import unittest

class TestClue(unittest.TestCase):

    def test_clue00(self):
        clu = Clue('if(a) {}')
        clu.parse()
        self.assertEqual([1, Fraction(0, 1)], clu.clue())

    def test_clue01(self):
        clu = Clue('if(a)')
        clu.parse()
        self.assertEqual([0, 0], clu.clue())

    def test_clue02(self):
        clu = Clue('if(a {}')
        clu.parse()
        self.assertEqual([0, 0], clu.clue())

    def test_clue03(self):
        clu = Clue('if(a) }')
        clu.parse()
        self.assertEqual([0, 0], clu.clue())

    def test_clue04(self):
        clu = Clue('if(a)')
        clu.parse()
        self.assertEqual([0, 0], clu.clue())

    def test_clue04curl(self):
        clu = Clue('if(b){}')
        clu.parse()
        self.assertEqual([1, Fraction(0, 1)], clu.clue())


    def test_clue2(self):
        clu = Clue('if(a && b){}')
        clu.parse()
        self.assertEqual([1, Fraction(1,3)], clu.clue())

    def test_clue3(self):
        clu = Clue('if(a || b){}')
        clu.parse()
        self.assertEqual([1, Fraction(1,2)], clu.clue())

    def test_clue4(self):
        clu = Clue('if(a){ if (b) {}}')
        clu.parse()
        self.assertEqual([2, 0], clu.clue())

    def test_clue5(self):
        clu = Clue('if(a){ if (b) {}} if (c) {}')
        clu.parse()
        self.assertEqual([4, 0], clu.clue())

    def test_clu6(self):
        clu = Clue('for(int i=0; i<10; i++) {}')
        clu.parse()
        self.assertEqual([1, 0], clu.clue())

    def test_clu7(self):
        clu = Clue('while (i<10) {}')
        clu.parse()
        self.assertEqual([1, 0], clu.clue())

    def test_clu8(self):
        clu = Clue('if (a) {}')
        clu.parse()
        self.assertEqual(1, clu.subPathConjecture())

    def test_clu9(self):
        clu = Clue('if (a) { if (b) {}}')
        clu.parse()
        self.assertEqual(3, clu.subPathConjecture())


    def test_clu10_curl_space(self):
        clu = Clue('if (a) {}')
        clu.parse()
        self.assertEqual(2, clu.subPaths())


    def test_clu11(self):
        clu = Clue('if (a) { if (b) {} }')
        clu.parse()
        self.assertEqual(3, clu.subPaths())


    def test_self1_xi_post(self):
        code = '{ if (a) { } if (b) { } if (c) { } }'
        clu = Clue(code)
        clu.parse()
        parallel = clu.clue()

        code = '{ if (a) { if (b) { if (c) { } } } }'
        clu = Clue(code)
        clu.parse()
        orthogonal = clu.clue()

        self.assertEqual(True, orthogonal[0] < parallel[0]) 


    def test_colloc1_xi(self):
        code = 'if (-1<1) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, 0], clu.clue())

    def test_colloc1_cabe(self):
        code = 'if (-1<l) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.cabe())

    def test_colloc1_subPaths(self):
        code = 'if (-1<l) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.subPaths())

    def test_colloc1_subPathConjecture(self):
        code = 'if (-1<l) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(1, clu.subPathConjecture())


    def test_colloc_2_xi(self):
        code = 'if (3>l && 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, Fraction(1,3)], clu.clue())

    def test_colloc_2_cabe(self):
        code = 'if (3>l && 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.cabe())

    def test_colloc_2_subPaths(self):
        code = 'if (3>l && 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPaths())

    def test_colloc_2_subPathConjecture(self):
        code = 'if (3>l && 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPathConjecture())


    def test_colloc3_xi(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, Fraction(1,5)+Fraction(1,3)], clu.clue())

    def test_colloc3_cabe(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe())

    def test_colloc3_subPaths(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths())


    def test_colloc3_subPathConjecture(self):
        code = 'if (2>l && 7>k && 10>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPathConjecture())


    def test_colloc4_xi(self):
        code = 'if (2>l || 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, Fraction(1,2)], clu.clue())

    def test_colloc4_cabe(self):
        code = 'if (2>l || 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.cabe())


    def test_colloc4_subPaths(self):
        code = 'if (2>l || 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPaths())


    def test_colloc4_subPathConjecture(self):
        code = 'if (2>l || 0<k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPathConjecture())


    def test_colloc5_xi(self):
        code = 'if (0<l) { if (2>k) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([2, 0], clu.clue())

    def test_colloc5_cabe(self):
        code = 'if (0<l) { if (2>k) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.cabe())

    def test_colloc5_subPaths(self):
        code = 'if (0<l) { if (2>k) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPaths())

    def test_colloc5_subPathConjecture(self):
        code = 'if (0<l) { if (2>k) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPathConjecture())



    def test_colloc6_xi(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([2, Fraction(1,3)], clu.clue()) 

    def test_colloc6_cabe(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc6_subPaths(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths()) 

    def test_colloc6_subPathConjecture(self):
        code = 'if (0<l && 4>k) { if (11>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPathConjecture()) 


    def test_colloc7_xi(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, Fraction(2,3) + Fraction(2,4)], clu.clue()) 

    def test_colloc7_cabe(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc7_subPaths(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths()) 

    def test_colloc7_subPathConjecture(self):
        code = 'if (2>l && 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPathConjecture()) 


    def test_colloc8_xi(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, Fraction(2,2) + Fraction(2,5)], clu.clue()) 

    def test_colloc8_cabe(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc8_subPaths(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths()) 

    def test_colloc8_subPathConjecture(self):
        code = 'if (2>l || 0<k && 1>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPathConjecture()) 


    def test_colloc9_xi(self):
        code = 'if (2>l) {} if (8>k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([3, 0], clu.clue()) 

    def test_colloc9_cabe(self):
        code = 'if (2>l) {} if (8>k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.cabe()) 

    def test_colloc9_subPaths(self):
        code = 'if (2>l) {} if (8>k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths()) 

    def test_colloc9_subPathConjecture(self):
        code = 'if (2>l) {} if (8>k) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.subPathConjecture()) 


    def test_colloc10_xi(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, Fraction(1,4)+Fraction(1,2)], clu.clue()) 

    def test_colloc10_cabe(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc10_subPaths(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths()) 

    def test_colloc10_subPathConjecture(self):
        code = 'if (2>l || 0<k || 4>n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPathConjecture()) 


    def test_colloc11_xi(self):
        code = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([3, 0], clu.clue()) 

    def test_colloc11_cabe(self):
        code = 'if (2>l) { if (8>k) { if (0<n) {} } }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc11_subPaths(self):
        code = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPaths()) 

    def test_colloc11_subPathConjecture(self):
        code = 'if (2>l) { if (8>k) { if (2<n) {} } }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPathConjecture()) 


    def test_colloc12_xi(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([4, 0], clu.clue()) 

    def test_colloc12_cabe(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc12_subPaths(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(5, clu.subPaths()) 

    def test_colloc12_subPathConjecture(self):
        code = 'if (0<l) { if(4>k){} if (8>n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPathConjecture()) 


    def test_colloc13_xi(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([4, 0], clu.clue()) 

    def test_colloc13_cabe(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc13_subPaths(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(6, clu.subPaths()) 

    def test_colloc13_subPathConjecture(self):
        code = 'if (0<l) { if (8>k) { } } if (0<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPathConjecture()) 


    def test_colloc14_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([3, Fraction(1,3)], clu.clue()) 

    def test_colloc14_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc14_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(6, clu.subPaths()) 

    def test_colloc14_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPathConjecture()) 


    def test_colloc15_xi(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([4, 0], clu.clue()) 

    def test_colloc15_cabe(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc15_subPaths(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(6, clu.subPaths()) 

    def test_colloc15_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k) { if (1<n) {} }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.subPathConjecture()) 


    def test_colloc16_xi(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([6, 0], clu.clue()) 

    def test_colloc16_cabe(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(4, clu.cabe()) 

    def test_colloc16_subPaths(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(8, clu.subPaths()) 

    def test_colloc16_subPathConjecture(self):
        code = 'if (-4<1) {} if (4<k) {} if (8>n) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(3, clu.subPathConjecture()) 


    def test_colloc17_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([6, Fraction(1,3)+Fraction(1,2)], clu.clue()) 

    def test_colloc17_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(6, clu.cabe()) 

    def test_colloc17_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(18, clu.subPaths()) 

    def test_colloc17_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n || 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(7, clu.subPathConjecture()) 


    def test_colloc18_xi(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([6, Fraction(1,3)+Fraction(1,3)], clu.clue()) 

    def test_colloc18_cabe(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(6, clu.cabe()) 

    def test_colloc18_subPaths(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(18, clu.subPaths()) 

    def test_colloc18_subPathConjecture(self):
        code = 'if (0<1) {} if (9>k && 1<n) { } if (2==n && 9>f) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(7, clu.subPathConjecture()) 


    def test_for_xi(self):
        code = 'for (int i; i<=9; i++) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, 0], clu.clue())

    def test_for_babe(self):
        code = 'for (int i; i<=9; i++) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.cabe())

    def test_for_subPaths(self):
        code = 'for (int i; i<=9; i++) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.cabe())

    def test_while_xi(self):
        code = 'while (i<=9) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([1, 0], clu.clue())

    def test_while_cabe(self):
        code = 'while (i<=9) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.cabe())

    def test_while_subPaths(self):
        code = 'while (i<=9) { }'
        clu = Clue(code)
        clu.parse()
        self.assertEqual(2, clu.subPaths())


    def test_clupath_1(self):
        code = 'if (a) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([[1, [0]]], clu.path())

    def test_clupath_2(self):
        code = 'if (a && b) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([[1, [Fraction(1,3)]]], clu.path())

    def test_clupath_3(self):
        code = 'if (a || b) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([[1, [Fraction(1, 2)]]], clu.path())

    def test_clupath_4(self):
        code = 'if (a) { if (b) {}} if (c) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([[1,[0]], [1, [0]], [2, [0]]], clu.path())

    def test_clupath_5(self):
        code = 'if (a && b || c && d) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([[1, [Fraction(2,5), Fraction(3,2), Fraction(2,5)]]], clu.path()) 

    def test_clupath6(self):
        code = 'if (a) { if (b) {} } if (c && c1) {} if (d || d1) {} if (e) {}'
        clu = Clue(code)
        clu.parse()
        self.assertEqual([[1, [0]], [1, [0]], [2, [Fraction(1,3)]], [3, [Fraction(1,2)]], [4, [0]]], clu.path())

    def test_verify1(self):
        code = 'if (a) {}'
        clu = Clue(code)
        clu.parse()
        self.assertTrue(clu.verify().startswith('[0]'))

    def test_verify2(self):
        code = 'if (a) {} if (b) {}'
        clu = Clue(code)
        clu.parse()
        self.assertTrue('[0]' in clu.verify() and '[9]' in clu.verify())


if __name__ == '__main__':
    unittest.main()
