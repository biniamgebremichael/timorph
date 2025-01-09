import unittest
from  gparser.TFST import TFST
from  Geez2Sera import Geez2Sera

from pyfoma import FST



class TestTFST(unittest.TestCase):

    variable = {'V': FST.re("[aeiouIE]"),
                'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWAO]")}
    def testPyfoma(self):
        fst = FST.re("$^rewrite((I):a / $C e $C _ $C a $C $V #,  leftmost = True) @ $^rewrite((a):I / $C e $C a $C _ $C $V #,  leftmost = True)  @ $^rewrite($V:(Iti) / $C e $C a $C I $C _ # )  ",TestTFST.variable)
        self.assertEqual(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መጽሓፍ")))[0]), "መጻሕፍቲ")
        self.assertEqual(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መዋእል")))[0]), "መዋእልቲ")
        self.assertEqual(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መውዓሊ")))[0]), "መዋዕልቲ")
        self.assertEqual(Geez2Sera.sera2geez(list(fst.generate(Geez2Sera.geez2sera("መልኣኽ")))[0]), "መላእኽቲ")
    def test_generate(self):
        src = Geez2Sera.geez2sera("ኣውጸአ")
        rule = "-2e_i @ e_omIni"
        tfst = TFST(rule)
        self.assertEqual(tfst.rule,"$^rewrite((e):(i) /  _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(omIni) /  _  # ,longest = True, leftmost = True )")
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate(src))[0]), "ኣውጺኦምኒ")

    def test_generate2(self):
        rule = "I_IkInI @ a_aKInI @ i_iKInI @ u_uKInI @ E_EKInI @ o_oKInI @ e_eKInI "
        tfst = TFST(rule)
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("ድሙ")))[0]), "ድሙኽን")
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("ቤት")))[0]), "ቤትክን")


    def test_prular(self):
        rule = "I_IkInI @ a_aKInI @ i_iKInI @ u_uKInI @ E_EKInI @ o_oKInI @ e_eKInI "
        tfst = TFST(rule)
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("መፍትሕ")))[0]), "መፋትሕ")
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("መጽሓፍ")))[0]), "መጻሕፍቲ")
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate( Geez2Sera.geez2sera("ቤት")))[0]), "ቤትክን")
    def test_generate_passive(self):
        src = Geez2Sera.geez2sera("ረኸበ")
        tfst = TFST.generate_passive(src)
        self.assertEqual(Geez2Sera.sera2geez(tfst), "ኣርከበ")

    def test_generate_noun_from_verb(self):
        src = Geez2Sera.geez2sera("ሰረቐ")
        tfst = TFST.generate_noun_from_verb(src)
        self.assertEqual(Geez2Sera.sera2geez(tfst), "ምስራቕ")

    def test_generate_noun_from_verb2(self):
        src = Geez2Sera.geez2sera("ረኸበ")
        tfst = TFST("0tI_ @ 0q_Q @ 0k_K @ 2q_Q @ 2K_k @ 1e_I @ 1a_I @ 0_Aa")
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate(src))[0]), "ኣርከበ")

if __name__ == '__main__':
    unittest.main()