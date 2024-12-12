
from pyfoma import FST

from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
class GeezFst:


    variable = {}
    def __init__(self,):
    
        self.variable = {'V': FST.re("[aeiouIE]"),
                    'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQW]"),
                    "empty": FST.re("$^rewrite(a:a)"),
                    "6e_u": FST.re("$^rewrite((e):u /  _ #      ,longest = True, leftmost = True )"),
                    "6e_o": FST.re("$^rewrite((e):o /  _ #      ,longest = True, leftmost = True )"),
                    "6e_om": FST.re("$^rewrite((e):(omI) /  _ # ,longest = True, leftmost = True )"),
                    "6e_ka": FST.re("$^rewrite((e):(Ika) /  _ # ,longest = True, leftmost = True )"),
                    "6e_ki": FST.re("$^rewrite((e):(Iki) /  _ # ,longest = True, leftmost = True )"),
                    "6_t": FST.re("$^rewrite('':(tI) / _ #      ,longest = True, leftmost = True )"),
                    "6_n": FST.re("$^rewrite('':(nI) / _  #     ,longest = True, leftmost = True )"),
                    "6_na": FST.re("$^rewrite('':(na) / e  _  # ,longest = True, leftmost = True )"),
                    "6e_a": FST.re("$^rewrite(e:(a) / _ #       ,longest = True, leftmost = True )"),
                    "6e_kum": FST.re("$^rewrite(e:(IkumI) / _  #,longest = True, leftmost = True )"),
                    "6e_kn": FST.re("$^rewrite(e:(IkInI) / _ #  ,longest = True, leftmost = True )"),
                    "_ni": FST.re("$^rewrite('':(ni)  / _  #    ,longest = True, leftmost = True )"),
                    "n_nani": FST.re("$^rewrite('I':(ani) / n _ #,longest = True, leftmost = True )"),
                    "_tni": FST.re("$^rewrite('':(tIni)  / _  # ,longest = True, leftmost = True )"),
                    "_tna": FST.re("$^rewrite('':(tIna)  / _  # ,longest = True, leftmost = True )"),
                    "i_ni": FST.re("$^rewrite('i':(Ini) / ki _ #,longest = True, leftmost = True )"),
                    "_yo": FST.re("$^rewrite('':(yo) / _  #     ,longest = True, leftmost = True )"),
                    "_to": FST.re("$^rewrite('':(to) / _  #     ,longest = True, leftmost = True )"),
                    "_wo": FST.re("$^rewrite('':(wo) / _  #     ,longest = True, leftmost = True )"),
                    "_1o": FST.re("$^rewrite('':(1o) / _  #     ,longest = True, leftmost = True )"),
                    "_mo": FST.re("$^rewrite('':(mo) / _  #     ,longest = True, leftmost = True )"),
                    "_o": FST.re("$^rewrite('I':(o) / _  #       ,longest = True, leftmost = True )"),
                    "_ya": FST.re("$^rewrite('':(ya) / _  #     ,longest = True, leftmost = True )"),
                    "_ta": FST.re("$^rewrite('':(ta) / _  #     ,longest = True, leftmost = True )"),
                    "_wa": FST.re("$^rewrite('':(wa) / _  #     ,longest = True, leftmost = True )"),
                    "_1a": FST.re("$^rewrite('':(1a) / _  #     ,longest = True, leftmost = True )"),
                    "_ma": FST.re("$^rewrite('':(ma) / _  #     ,longest = True, leftmost = True )"),
                    "_na": FST.re("$^rewrite('':(na) / _  #     ,longest = True, leftmost = True )"),
                    "e_na": FST.re("$^rewrite('e':(Ina) / _  #  ,longest = True, leftmost = True )"),
                    "_a": FST.re("$^rewrite('I':(a) / _  #      ,longest = True, leftmost = True )")
                    }
        
        self.variable["2e_i"] = FST.re("$^rewrite((e):i /  _ $C$V #  ,longest = True, leftmost = True )", self.variable)
        self.variable["2e_a"] = FST.re("$^rewrite((e):a /  _ $C$V #  ,longest = True, leftmost = True )", self.variable)
        self.variable["e_k"] = FST.re("$^rewrite(($V):(IkI) /  _  #   ,longest = True, leftmost = True )" ,self.variable)
        self.variable["IMP"] = FST.re("$^rewrite(($V):'I' / _ $C$V # ,longest = True, leftmost = True ) @ $^rewrite(($V):(o) / _  # ,longest = True, leftmost = True )", self.variable)



    def passive(self,word):
        passive = FST.re("$^rewrite(($V):'I' / # $C _   )  @ $^rewrite((tI):''  / # _   )  @   $^rewrite('':(1a) / # _   ) ", self.variable)

        return   list(passive.generate(word))[0]

    def ccc_verbs_test (self):
        fsts = {}
        fsts["PRE"] = {}
        fsts["PAS"] = {}
        fsts["PRE"]["N"] = {}
        fsts["PAS"]["N"] = {}
        fsts["PRE"]["N"]["I"] =  FST.re("$2e_i @ $e_k @ $_na @ $_na", self.variable)
        fsts["PAS"]["N"]["I"] =  FST.re("$2e_i @ $e_k @ $_na @ $_na ", self.variable)
        return fsts


    def ccc_verbs(self):
        fsts = {}
        fsts["PRE"] = {}
        fsts["PAS"] = {}
        fsts["PRE"]["N"] = {}
        fsts["PAS"]["N"] = {}
        fsts["PRE"]["N"]["I"] = self.variable['2e_i']
        fsts["PAS"]["N"]["I"] = self.variable["2e_i"]
        fsts["PRE"]["N"]["HE"] = self.variable["empty"]
        fsts["PAS"]["N"]["HE"] = FST.re("$2e_i @ $6e_u", self.variable)
        fsts["PRE"]["N"]["SHE"] = self.variable["6_t"]
        fsts["PAS"]["N"]["SHE"] = FST.re("$2e_i @ $6e_a", self.variable)
        fsts["PRE"]["N"]["WE"] = self.variable["6_na"]
        fsts["PAS"]["N"]["WE"] = FST.re("$2e_i @ $6_na", self.variable)
        fsts["PRE"]["N"]["THEY_M"] = self.variable["6e_u"]
        fsts["PAS"]["N"]["THEY_M"] = FST.re("$2e_i @ $6e_om", self.variable)
        fsts["PRE"]["N"]["THEY_F"] = self.variable["6e_a"]
        fsts["PAS"]["N"]["THEY_F"] = FST.re("$2e_i @ $6_n", self.variable)
        fsts["PRE"]["N"]["YOU_SM"] = self.variable["6e_ka"]
        fsts["PAS"]["N"]["YOU_SM"] = FST.re("$2e_i @ $6e_ka", self.variable)
        fsts["PRE"]["N"]["YOU_SF"] = self.variable["6e_ki"]
        fsts["PAS"]["N"]["YOU_SF"] = FST.re("$2e_i @ $6e_ki", self.variable)
        fsts["PRE"]["N"]["YOU_PM"] = self.variable["6e_kum"]
        fsts["PAS"]["N"]["YOU_PM"] = FST.re("$2e_i @ $6e_kum", self.variable)
        fsts["PRE"]["N"]["YOU_PF"] = self.variable["6e_kn"]
        fsts["PAS"]["N"]["YOU_PF"] = FST.re("$2e_i @ $6e_kn", self.variable)
    
        fsts["PRE"]["ME"] = {}
        fsts["PAS"]["ME"] = {}
        fsts["PRE"]["ME"]["I"] = self.variable["2e_i"]
        fsts["PAS"]["ME"]["I"] = self.variable["2e_i"]
        fsts["PRE"]["ME"]["HE"] = self.variable["_ni"]
        fsts["PAS"]["ME"]["HE"] = FST.re("$2e_i @ $6e_u @ $_ni", self.variable)
        fsts["PRE"]["ME"]["SHE"] = FST.re("$6_t @ $_ni", self.variable)
        fsts["PAS"]["ME"]["SHE"] = FST.re("$2e_i @ $6e_a  @ $_tni", self.variable)
        fsts["PRE"]["ME"]["WE"] = FST.re("$6_na  ", self.variable)
        fsts["PAS"]["ME"]["WE"] = FST.re("$2e_i @ $6_na  ", self.variable)
        fsts["PRE"]["ME"]["THEY_M"] = FST.re("$6e_u @ $_ni", self.variable)
        fsts["PAS"]["ME"]["THEY_M"] = FST.re("$2e_i @ $6e_om @ $_ni", self.variable)
        fsts["PRE"]["ME"]["THEY_F"] = FST.re("$6e_a @ $_ni", self.variable)
        fsts["PAS"]["ME"]["THEY_F"] = FST.re("$2e_i @ $6_na @ $_ni", self.variable)
        fsts["PRE"]["ME"]["YOU_SM"] = FST.re("$6e_ka  @ $_ni", self.variable)
        fsts["PAS"]["ME"]["YOU_SM"] = FST.re("$2e_i @ $6e_ka  @ $_ni", self.variable)
        fsts["PRE"]["ME"]["YOU_SF"] = FST.re("$6e_ki @ $i_ni", self.variable)
        fsts["PAS"]["ME"]["YOU_SF"] = FST.re("$2e_i @ $6e_ki @ $i_ni", self.variable)
        fsts["PRE"]["ME"]["YOU_PM"] = FST.re("$6e_kum @ $_ni", self.variable)
        fsts["PAS"]["ME"]["YOU_PM"] = FST.re("$2e_i @ $6e_kum @ $_ni", self.variable)
        fsts["PRE"]["ME"]["YOU_PF"] = FST.re("$6e_kn @ $n_nani", self.variable)
        fsts["PAS"]["ME"]["YOU_PF"] = FST.re("$2e_i @ $6e_kn @ $n_nani", self.variable)
    
    
        fsts["PRE"]["HIM"] = {}
        fsts["PAS"]["HIM"] = {}
        fsts["PRE"]["HIM"]["I"] = FST.re("$2e_i @ $_yo", self.variable)
        fsts["PAS"]["HIM"]["I"] = FST.re("$2e_i @ $_yo", self.variable)
        fsts["PRE"]["HIM"]["HE"] = FST.re("$6e_o", self.variable)
        fsts["PAS"]["HIM"]["HE"] = FST.re("$2e_i @ $6e_u @ $_wo", self.variable)
        fsts["PRE"]["HIM"]["SHE"] = FST.re("$6_t @ $_o", self.variable)
        fsts["PAS"]["HIM"]["SHE"] = FST.re("$2e_i @ $6e_a  @ $_to", self.variable)
        fsts["PRE"]["HIM"]["WE"] = FST.re("$6_na @ $_yo", self.variable)
        fsts["PAS"]["HIM"]["WE"] = FST.re("$2e_i @ $6_na @ $_yo", self.variable)
        fsts["PRE"]["HIM"]["THEY_M"] = FST.re("$6e_u @ $_wo", self.variable)
        fsts["PAS"]["HIM"]["THEY_M"] = FST.re("$2e_i @ $6e_om @ $_wo", self.variable)
        fsts["PRE"]["HIM"]["THEY_F"] = FST.re("$6e_a @ $_1o", self.variable)
        fsts["PAS"]["HIM"]["THEY_F"] = FST.re("$2e_i @ $6_n @ $_1o", self.variable)
        fsts["PRE"]["HIM"]["YOU_SM"] = FST.re("$6e_ka  @ $_yo", self.variable)
        fsts["PAS"]["HIM"]["YOU_SM"] = FST.re("$2e_i @ $6e_ka  @ $_yo", self.variable)
        fsts["PRE"]["HIM"]["YOU_SF"] = FST.re("$6e_ki @ $_yo", self.variable)
        fsts["PAS"]["HIM"]["YOU_SF"] = FST.re("$2e_i @ $6e_ki @ $_yo", self.variable)
        fsts["PRE"]["HIM"]["YOU_PM"] = FST.re("$6e_kum @ $_wo", self.variable)
        fsts["PAS"]["HIM"]["YOU_PM"] = FST.re("$2e_i @ $6e_kum @ $_wo", self.variable)
        fsts["PRE"]["HIM"]["YOU_PF"] = FST.re("$6e_kn @ $_1o", self.variable)
        fsts["PAS"]["HIM"]["YOU_PF"] = FST.re("$2e_i @ $6e_kn @ $_1o", self.variable)
    
    
        fsts["PRE"]["HER"] = {}
        fsts["PAS"]["HER"] = {}
        fsts["PRE"]["HER"]["I"] = FST.re("$2e_i @ $_ya", self.variable)
        fsts["PAS"]["HER"]["I"] = FST.re("$2e_i @ $_ya", self.variable)
        fsts["PRE"]["HER"]["HE"] = FST.re("$6e_a", self.variable)
        fsts["PAS"]["HER"]["HE"] = FST.re("$2e_i @ $6e_u @ $_wa", self.variable)
        fsts["PRE"]["HER"]["SHE"] = FST.re("$6_t @ $_a", self.variable)
        fsts["PAS"]["HER"]["SHE"] = FST.re("$2e_i @ $6e_a  @ $_ta", self.variable)
        fsts["PRE"]["HER"]["WE"] = FST.re("$6_na @ $_ya", self.variable)
        fsts["PAS"]["HER"]["WE"] = FST.re("$2e_i @ $6_na @ $_ya", self.variable)
        fsts["PRE"]["HER"]["THEY_M"] = FST.re("$6e_u @ $_wa", self.variable)
        fsts["PAS"]["HER"]["THEY_M"] = FST.re("$2e_i @ $6e_om @ $_wa", self.variable)
        fsts["PRE"]["HER"]["THEY_F"] = FST.re("$6e_a @ $_1a", self.variable)
        fsts["PAS"]["HER"]["THEY_F"] = FST.re("$2e_i @ $6_n @ $_1a", self.variable)
        fsts["PRE"]["HER"]["YOU_SM"] = FST.re("$6e_ka  @ $_ya", self.variable)
        fsts["PAS"]["HER"]["YOU_SM"] = FST.re("$2e_i @ $6e_ka  @ $_ya", self.variable)
        fsts["PRE"]["HER"]["YOU_SF"] = FST.re("$6e_ki @ $_ya", self.variable)
        fsts["PAS"]["HER"]["YOU_SF"] = FST.re("$2e_i @ $6e_ki @ $_ya", self.variable)
        fsts["PRE"]["HER"]["YOU_PM"] = FST.re("$6e_kum @ $_wa", self.variable)
        fsts["PAS"]["HER"]["YOU_PM"] = FST.re("$2e_i @ $6e_kum @ $_wa", self.variable)
        fsts["PRE"]["HER"]["YOU_PF"] = FST.re("$6e_kn @ $_1a", self.variable)
        fsts["PAS"]["HER"]["YOU_PF"] = FST.re("$2e_i @ $6e_kn @ $_1a", self.variable)
    
        fsts["PRE"]["US"] = {}
        fsts["PAS"]["US"] = {}
        fsts["PRE"]["US"]["I"] = FST.re("$empty", self.variable)
        fsts["PAS"]["US"]["I"] = FST.re("$2e_i", self.variable)
        fsts["PRE"]["US"]["HE"] = FST.re("$_na ", self.variable)
        fsts["PAS"]["US"]["HE"] = FST.re("$2e_i @ $_na", self.variable)
        fsts["PRE"]["US"]["SHE"] = FST.re("$_tna", self.variable)
        fsts["PAS"]["US"]["SHE"] = FST.re("$2e_i @ $_tna", self.variable)
        fsts["PRE"]["US"]["WE"] = FST.re("$e_na", self.variable)
        fsts["PAS"]["US"]["WE"] = FST.re("$2e_i @ $e_na", self.variable)
        fsts["PRE"]["US"]["THEY_M"] = FST.re("$6e_u @ $_na", self.variable)
        fsts["PAS"]["US"]["THEY_M"] = FST.re("$2e_i @ $6e_u @ $_na", self.variable)
        fsts["PRE"]["US"]["THEY_F"] = FST.re("$6e_a @ $_na", self.variable)
        fsts["PAS"]["US"]["THEY_F"] = FST.re("$2e_i @ $_na @ $_na", self.variable)
        fsts["PRE"]["US"]["YOU_SM"] = FST.re("$6e_ka  @ $_na", self.variable)
        fsts["PAS"]["US"]["YOU_SM"] = FST.re("$2e_i @ $6e_ka  @ $_na", self.variable)
        fsts["PRE"]["US"]["YOU_SF"] = FST.re("$6e_ki @ $_na", self.variable)
        fsts["PAS"]["US"]["YOU_SF"] = FST.re("$2e_i @ $e_k @ $_na", self.variable)
        fsts["PRE"]["US"]["YOU_PM"] = FST.re("$6e_kum @ $_na", self.variable)
        fsts["PAS"]["US"]["YOU_PM"] = FST.re("$2e_i @ $6e_kum @ $_na", self.variable)
        fsts["PRE"]["US"]["YOU_PF"] = FST.re("$e_k @ $_na @ $_na", self.variable)
        fsts["PAS"]["US"]["YOU_PF"] = FST.re("$2e_i @ $e_k @ $_na @ $_na", self.variable)
    
    
        return fsts

    def generate_all(self, word):
        word_rows = {}
        score = 0
        total = 0
        fsts = self.ccc_verbs()
        for tense in fsts:
            row = {}
            row['OBJECT'] = []
            for object in fsts[tense]:
                row['OBJECT'].append(object)
                for subject in fsts[tense][object]:
                    p = fsts[tense][object][subject]
                    if not subject in row:
                        row[subject] = []
                    result_pre = list(p.generate(word))[0]
                    score += GeezScore.exists(Geez2Sera.sera2geez(result_pre))
                    total += 1
                    row[subject].append(result_pre)
            word_rows[tense] = row
        return word_rows, int((score * 100) / total)
