import re
from pyfoma import FST


class TFST:

    variable = {'V': FST.re("[aeiouIE]"),
                'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNTZCPSQWAO]")}
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

