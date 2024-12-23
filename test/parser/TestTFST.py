import unittest
from  gparser.TFST import TFST
from  Geez2Sera import Geez2Sera

def add(x, y):
    return x + y

class TestTFST(unittest.TestCase):
    def test_generate(self):
        src = Geez2Sera.geez2sera("ኣውጸአ")
        rule = "-2e_i @ e_omIni"
        tfst = TFST(rule)
        self.assertEqual(tfst.rule,"$^rewrite((e):(i) /  _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite((e):(omIni) /  _  # ,longest = True, leftmost = True )")
        self.assertEqual(Geez2Sera.sera2geez(list(tfst.generate(src))[0]), "ኣውጺኦምኒ")


    def test_generate_passive(self):
        src = Geez2Sera.geez2sera("ረኸበ")
        tfst = TFST.generate_passive(src)
        self.assertEqual(Geez2Sera.sera2geez(tfst), "ኣርከበ")

    def test_generate_noun_from_verb(self):
        src = Geez2Sera.geez2sera("ሰረቐ")
        tfst = TFST.generate_noun_from_verb(src)
        self.assertEqual(Geez2Sera.sera2geez(tfst), "ምስራቕ")
    def test_generate_noun_from_verb(self):
        src = Geez2Sera.geez2sera("ኣሰረ")
        tfst = TFST.generate_noun_from_verb(src)
        self.assertEqual(Geez2Sera.sera2geez(tfst), "ምእሳር")
    def test_generate_noun_from_verb2(self):
        src = Geez2Sera.geez2sera("ረኸበ")
        tfst = TFST.generate_noun_from_verb(src)
        self.assertEqual(Geez2Sera.sera2geez(tfst), "ምርካብ")

if __name__ == '__main__':
    unittest.main()