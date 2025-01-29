import unittest
from gparser.TFST import TFST
from Geez2Sera import Geez2Sera

from pyfoma import FST


class TestTFST(unittest.TestCase):
    variable = {'V': FST.re("[aeiouIE]"),
                'K': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWT]"),
                'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWAOT]")}

    def test_rule_generator2(self):
        self.assertEqual("$^rewrite((e):(Iku) / _ # ,longest = True, leftmost = True )", TFST._generate2("e_Iku"))
        self.assertEqual("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True )", TFST._generate2("-2e_i") )
        self.assertEqual("$^rewrite((e):(IkIwo) / _ # ,longest = True, leftmost = True )", TFST._generate2("e_IkIwo") )
        self.assertEqual("$^rewrite((''):(ni) / _ # ,longest = True, leftmost = True )", TFST._generate2("_ni"))
        self.assertEqual("$^rewrite(($V):(ItatI) / _ # ,longest = True, leftmost = True )",TFST._generate2("$V_ItatI") )
        self.assertEqual("$^rewrite((''):(ti) / # _ ,shortest = True, leftmost = True )",TFST._generate2("0_ti") )

    def assertEqualIgnoreSpace(self,x,y):
        self.assertEqual(" ".join(x.split())," ".join(y.split()))
    def test_rule_generator(self):

        self.assertEqualIgnoreSpace("$^rewrite((''):(ti) / # _ ,shortest = True, leftmost = True )",TFST("0_ti").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(Iku) / _ # ,longest = True, leftmost = True )", TFST("e_Iku").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True )", TFST("-2e_i").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIwo) / _ # ,longest = True, leftmost = True )", TFST("e_IkIwo").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIwa) / _ # ,longest = True, leftmost = True )", TFST("e_IkIwa").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True )", TFST("-2e_i").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIwomI) / _ # ,longest = True, leftmost = True )", TFST("e_IkIwomI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIwenI) / _ # ,longest = True, leftmost = True )", TFST("e_IkIwenI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((''):(ni) / _ # ,longest = True, leftmost = True )", TFST("_ni").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(o) / _ # ,longest = True, leftmost = True )", TFST("e_o").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(a) / _ # ,longest = True, leftmost = True )", TFST("e_a").rule)
        self.assertEqualIgnoreSpace("$^rewrite((''):(na) / _ # ,longest = True, leftmost = True )", TFST("_na").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(omI) / _ # ,longest = True, leftmost = True )", TFST("e_omI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((''):(tIki) / _ # ,longest = True, leftmost = True )", TFST("_tIki").rule)
        self.assertEqualIgnoreSpace("$^rewrite((''):(tIkumI) / _ # ,longest = True, leftmost = True )", TFST("_tIkumI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((''):(tenI) / _ # ,longest = True, leftmost = True )", TFST("_tenI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(Ina) / _ # ,longest = True, leftmost = True )", TFST("e_Ina").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(InakumI) / _ # ,longest = True, leftmost = True )", TFST("e_InakumI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(InakInI) / _ # ,longest = True, leftmost = True )", TFST("e_InakInI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(u) / _ # ,longest = True, leftmost = True )", TFST("e_u").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(uni) / _ # ,longest = True, leftmost = True )", TFST("e_uni").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(uwo) / _ # ,longest = True, leftmost = True )", TFST("e_uwo").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(uwa) / _ # ,longest = True, leftmost = True )", TFST("e_uwa").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IAa) / _ # ,longest = True, leftmost = True )", TFST("e_IAa").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(ana) / _ # ,longest = True, leftmost = True )", TFST("e_ana").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIni) / _ # ,longest = True, leftmost = True )", TFST("e_IkIni").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIyo) / _ # ,longest = True, leftmost = True )", TFST("e_IkIyo").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIya) / _ # ,longest = True, leftmost = True )", TFST("e_IkIya").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIna) / _ # ,longest = True, leftmost = True )", TFST("e_IkIna").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIyomI) / _ # ,longest = True, leftmost = True )", TFST("e_IkIyomI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkIyenI) / _ # ,longest = True, leftmost = True )", TFST("e_IkIyenI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkumIwa) / _ # ,longest = True, leftmost = True )", TFST("e_IkumIwa").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkInIAomI) / _ # ,longest = True, leftmost = True )", TFST("e_IkInIAomI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(IkInIAenI) / _ # ,longest = True, leftmost = True )", TFST("e_IkInIAenI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True )",TFST("-2e_i").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True )",TFST("-2e_i").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(yo) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _yo").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(yomI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _yomI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(kumI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _kumI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(kInI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _kInI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(Ika) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_Ika").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(uki) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_uki").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(IkumI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_IkumI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(I) / _ # ,longest = True, leftmost = True ) @ $^rewrite((''):(kInI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_I @ _kInI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(a) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_a").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(Ina) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_Ina").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(Inayo) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_Inayo").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(Inaya) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_Inaya").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(Ina) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_Ina").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(InayomI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_InayomI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(omuna) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ e_omuna").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(momI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _momI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite(($V):(omIkInI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ $V_omIkInI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(nI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _nI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(nani) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _nani").rule)
        self.assertEqualIgnoreSpace("$^rewrite((e):(i) / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((''):(nIAenI) / _ # ,longest = True, leftmost = True )",TFST("-2e_i @ _nIAenI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((I):(eyI) / _ # ,longest = True, leftmost = True ) @ $^rewrite((u):(oyI) / _ # ,longest = True, leftmost = True ) @ $^rewrite((E):(EyI) / _ # ,longest = True, leftmost = True ) @ $^rewrite((a):(ayI) / _ # ,longest = True, leftmost = True ) @ $^rewrite((i):(eyI) / _ # ,longest = True, leftmost = True ) @ $^rewrite((e):(eyI) / _ # ,longest = True, leftmost = True ) @ $^rewrite((o):(oyI) / _ # ,longest = True, leftmost = True )",TFST("I_eyI @ u_oyI @ E_EyI @ a_ayI @ i_eyI @ e_eyI @ o_oyI").rule)
        self.assertEqualIgnoreSpace("$^rewrite((u):(IAu) / _ # ,longest = True, leftmost = True ) @ $^rewrite((E):(EAu) / _ # ,longest = True, leftmost = True ) @ $^rewrite((a):(aAu) / _ # ,longest = True, leftmost = True ) @ $^rewrite((I):(u) / _ # ,longest = True, leftmost = True ) @ $^rewrite((i):(u) / _ # ,longest = True, leftmost = True ) @ $^rewrite((e):(eAu) / _ # ,longest = True, leftmost = True ) @ $^rewrite((o):(oAu) / _ # ,longest = True, leftmost = True )",TFST("u_IAu @ E_EAu @ a_aAu @ I_u @ i_u @ e_eAu @ o_oAu").rule)
        self.assertEqualIgnoreSpace("$^rewrite((a):(aAa) / _ # ,longest = True, leftmost = True ) @ $^rewrite((u):(uAa) / _ # ,longest = True, leftmost = True ) @ $^rewrite((E):(EAa) / _ # ,longest = True, leftmost = True ) @ $^rewrite((I):(a) / _ # ,longest = True, leftmost = True ) @ $^rewrite((i):(a) / _ # ,longest = True, leftmost = True ) @ $^rewrite((e):(eAa) / _ # ,longest = True, leftmost = True ) @ $^rewrite((o):(oAa) / _ # ,longest = True, leftmost = True )",TFST("a_aAa @ u_uAa @ E_EAa @ I_a @ i_a @ e_eAa @ o_oAa").rule)
        self.assertEqualIgnoreSpace("$^rewrite((i):(I) / _ # ,longest = True, leftmost = True ) @ $^rewrite((''):(na) / _ # ,longest = True, leftmost = True )",TFST("i_I @ _na").rule)
        self.assertEqualIgnoreSpace("$^rewrite(($V):(atI) / _ # ,longest = True, leftmost = True )",TFST("$V_atI").rule)
        self.assertEqualIgnoreSpace("$^rewrite(($V):(ItatI) / _ # ,longest = True, leftmost = True )",TFST("$V_ItatI").rule)
