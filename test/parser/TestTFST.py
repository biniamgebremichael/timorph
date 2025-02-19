import unittest
from  gparser.TFST import TFST
from gparser.Geez2Sera import Geez2Sera

from pyfoma import FST



class TestTFST(unittest.TestCase):

    variable = {'V': FST.re("[aeiouIE]"),
                'K': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWT]"),
                'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWAOT]")}

    def assertEqualIgnoreSpace(self,x,y):
        self.assertEqual(" ".join(x.split())," ".join(y.split()))
        
    def test_rule_generator(self):
        self.assertEqualIgnoreSpace("$^rewrite((e):(a) / _ $C$V # ,longest = True, leftmost = True )", TFST._generate("-2e_a"))
    def testPyfoma(self):
        CeCICaCV = " $^rewrite((a):I / $C e $C I $C _ $C $V # )  @ $^rewrite($V:(Iti) / # $C e $C I $C I $C _ # )  @ $^rewrite((I):a / $C e $C _ $C I $C $V t $V # )"
        _at = " $^rewrite($V:(atI) /   $C _ # ) "
        _tat = " $^rewrite($V:(ItatI) /   $C _ # ) "
        CeCiNa= "$^rewrite(i:(ayI) / $C e $C _ $C a # ) @ $^rewrite(a:I / $C e $C a y I $C _ # )"
        AeCINV= "$^rewrite($V:(eAI) / # A _ $C I $C $V # ) @ $^rewrite(I:a / # A e A I $C _ $C $V # )  @ $^rewrite($V:I / # A e A I $C a $C _ # )"
        CeCICV= "$^rewrite('':(Aa) / # _ $C e $C I $C $V # ) @  $^rewrite('e':a / # A a $C _ $C I $C $V  ) @  $^rewrite($V:I /   A a $C a $C I $C _ # )"
        CeCeCV= "$^rewrite('':(Aa) / # _ $C e $C e $C $V # ) @  $^rewrite('e':I / # A a $C _ $C e $C $V  ) @  $^rewrite($V:a /   A a $C I $C _ $C $V # )"
        fst = FST.re(CeCICaCV ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መጽሓፍ")))[0]), "መጻሕፍቲ")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መውዓሊ")))[0]), "መዋዕልቲ")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መልኣኽ")))[0]), "መላእኽቲ")
        fst = FST.re(_at ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መዋእል")))[0]), "መዋእላት")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("ሃዋርያ")))[0]), "ሃዋርያት")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መዓልቲ")))[0]), "መዓልታት")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("ምስጢር")))[0]), "ምስጢራት")
        fst = FST.re(_tat ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("ነጥቢ")))[0]), "ነጥብታት")
        fst = FST.re( CeCiNa ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መኪና")))[0]), "መካይን")
        #fst = FST.re( CeCaCVCV+' @ '+CICICiCV+' @ '+CeCiNa+' @ '+AeCINV + '@' + CeCICV+ '@' + CeCeCV ,TestTFST.variable)
        fst = FST.re( AeCINV ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("እልፊ")))[0]), "አእላፍ")
        fst = FST.re( CeCICV ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("በትሪ")))[0]), "ኣባትር")
        fst = FST.re( CeCeCV ,TestTFST.variable)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("ፈረስ")))[0]), "ኣፍራስ")


    def test_generate(self):
        src = Geez2Sera.geez2sera("ኣውጸአ")
        rule = "-2e_i @ e_omIni"
        tfst = TFST(rule)
        self.assertEqualIgnoreSpace(tfst.rule,"$^rewrite((e):(i) /  _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(omIni) /  _  # ,longest = True, leftmost = True )")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate(src))[0]), "ኣውጺኦምኒ")

    def test_generate2(self):
        rule = "I_IkInI @ a_aKInI @ i_iKInI @ u_uKInI @ E_EKInI @ o_oKInI @ e_eKInI "
        tfst = TFST(rule)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("ድሙ")))[0]), "ድሙኽን")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("ቤት")))[0]), "ቤትክን")


    def test_prular(self):
        rule = "I_IkInI @ a_aKInI @ i_iKInI @ u_uKInI @ E_EKInI @ o_oKInI @ e_eKInI "
        tfst = TFST(rule)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("መፍትሕ")))[0]), "መፋትሕ")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("መጽሓፍ")))[0]), "መጻሕፍቲ")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("ቤት")))[0]), "ቤትክን")


    def test_generate_noun_plural(self):
        src = Geez2Sera.geez2sera("ሓኪም")
        rule = "$^rewrite((k):(K) / # $C $V _ i $C I  ) @ $^rewrite((i):(ayI) / # $C $V K _ $C I ) "
        dest = list(TFST(rule).generate(src))[0]
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(dest), "ሓኻይም")

    def test_generate_noun_from_verb2(self):
        src = Geez2Sera.geez2sera("ረኸበ")
        tfst = TFST("0tI_ @ 0q_Q @ 0k_K @ 2q_Q @ 2K_k @ 1e_I @ 1a_I @ 0_Aa")
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate(src))[0]), "ኣርከበ")


    def test_generate_consonant(self):
        src = Geez2Sera.geez2sera("ትለክሚ")
        rule = "-2lke_I"
        tfst = TFST(rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(I) / # $C$V l _ ,shortest = True, leftmost = True )",tfst.rule)
        self.assertEqualIgnoreSpace(Geez2Sera.sera2geez(list(tfst.generate(src))[0]), "ትልክሚ")

if __name__ == '__main__':
    unittest.main()