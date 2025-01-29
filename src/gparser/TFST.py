import re
from pyfoma import FST


class TFST:
    variable = {'V': FST.re("[aeiouIE]"),
                'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNTZCPSQWAO]"),
                'A': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNTZCPSQWO]")}

    def __init__(self, feature):
        if ("rewrite" in feature):
            self.rule = feature
        else:
            self.rule = TFST._getfst(feature)
        self.fst = FST.re(self.rule, TFST.variable)

    @staticmethod
    def init_position(p):
        if (p == None):
            return ""

        position = "$C"
        for i in range(1, int(p)):
            position = position + "$V$C"
        return position

    @staticmethod
    def _generate2(src):
        pattern = "^(\-){0,1}(\d){0,1}([^aeiouIE\\$]){0,1}(\\$*[aeiouIEV]*)([^aeiouIE\\$]){0,1}_(\w*)$"
        if (re.match(pattern, src.strip())):
            (d, p, c, f, k, t) = re.match(pattern, src.strip()).groups()
            f = f if f else "''"
            position = TFST.init_position(p)
            applied = "longest" if not p or (int(p) > 0 and d == '-') else "shortest"
            if (d == '-' or not p):
                return f"$^rewrite(({f}):({t or ''}) / {c or ''} _ {k or ''} {position} # ,{applied} = True, leftmost = True )"
            else:
                return f"$^rewrite(({f}):({t or ''}) / # {position} {c or ''} _ {k or ''}   ,{applied} = True, leftmost = True )"

        else:
            print(src, 'does not match')

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
                    if (c):
                        position = "# " + position + " _ ,shortest = True, leftmost = True"
                    else:
                        position = "# " + position + "$C  _ ,shortest = True, leftmost = True"
            elif (int(p) == 0):
                position = "# " + position + " _ ,shortest = True, leftmost = True"

            rewriter = "$^rewrite(({}):({}) / {} )".format(f if f else c if c else "''", t if t else "''", position)

            return " ".join(rewriter.split())
        else:
            print(src, 'does not match')

    @staticmethod
    def _getfst(feature):
        if ("@" in feature):
            return " @ ".join([TFST._generate(s) for s in feature.split("@")])
        else:
            return TFST._generate(feature)

    def generate(self, src):
        return self.fst.generate(src)
