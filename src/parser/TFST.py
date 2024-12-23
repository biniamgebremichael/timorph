import re
from pyfoma import FST


class TFST:

    variable = {'V': FST.re("[aeiouIE]"),
                'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWAO]")}
    def __init__(self, feature):
        self.feature = feature
        self.rule = TFST._getfst(feature)
        self.fst = FST.re(self.rule, TFST.variable)


    @staticmethod
    def _generate(src):
        pattern = "^(\-){0,1}(\d){0,1}([^aeiouIE]*)(\\$*[aeiouIEV]*)_(\w*)$"
        if (re.match(pattern, src.strip())):
            (d, p, c, f, t) = re.match(pattern, src.strip()).groups()
            position = ""
            if (p == None):
                position = " _  # ,longest = True, leftmost = True"
            elif (int(p) > 0):
                for i in range(1, int(p)):
                    position = position + "$C$V"
                if (d == '-'):
                    position = " _ " + position + " # ,longest = True, leftmost = True"
                else:
                    if(c):
                        position = "# " + position + " _ ,shortest = True, leftmost = True"
                    else:
                        position = "# " + position + "$C  _ ,shortest = True, leftmost = True"
            elif (int(p)==0):
                position = "# " + position + " _ ,shortest = True, leftmost = True"

            rewriter = "$^rewrite(({}):({}) / {} )".format(f if f else c if c else "''", t if t else "''", position)

            return rewriter
        else:
            print(src, 'does not match')
    @staticmethod
    def _getfst(feature):
        if ("@" in feature):
             return " @ ".join([TFST._generate(s) for s in  feature.split("@")])
        else:
             return TFST._generate(feature)

    def generate(self, src):
        return self.fst.generate(src)

    def isEmpty(self):
        return self.feature == '_'

    def toJSON(self):
        return self.feature

    @staticmethod
    def generate_passive(src):
        passive = "0tI_ @ 0q_Q @ 0k_K @ 2q_Q @ 2K_k @ 1e_I @ 1a_I @ 0_Aa"
        return  list(TFST(passive).generate(src))[0]

    @staticmethod
    def generate_noun_from_verb(src):
        passive = " 1e_I @ 1a_I @ -2$e_a @ -2$I_a @e_I @   2K_k @ 0_mI"
        return  list(TFST(passive).generate(src))[0]