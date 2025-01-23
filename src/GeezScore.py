import os,re
from Geez2Sera import Geez2Sera

class GeezScore:
    _top_words = set()
    _all_words = dict()
    _geez_3or4char = set()
    _geez_2char = set()
    _geez_cecece = set()
    _geez_caccc = set()
    score_file = os.path.join(os.path.dirname(__file__),  "resources/ti_score.txt")

    @staticmethod
    def is_cecece(word):
        # Define a regex pattern for consonant-vowel-consonant-vowel-consonant-vowel
        #pattern = r'^[^aeiouIE][\w][^aeiouIE][\w][^aeiouIE][\w]$'
        pattern = r'^[^aeiouIE][ea][^aeiouIE][ae][^aeiouIE][e]$'
        pattern2 = r'^[^aeiouIE][ea][^aeiouIE][aeiouIE][^aeiouIE][aeouIE][^aeiouIE][e]$'
        return bool(re.fullmatch(pattern, word)) or bool(re.fullmatch(pattern2, word))
    @staticmethod
    def is_caccc(word):
        # Define a regex pattern for consonant-vowel-consonant-vowel-consonant-vowel
        #pattern = r'^[^aeiouIE][\w][^aeiouIE][\w][^aeiouIE][\w]$'
        pattern2 = r'^[^aeiouIE][a][^aeiouIE][I][^aeiouIE][I][^aeinouIE][I]$'
        return bool(re.fullmatch(pattern2, word))

    @staticmethod
    def init():
        if len(GeezScore._all_words) <= 0 :
            f = open(GeezScore.score_file, encoding='utf-8')
            lines = f.readlines()

            for l in lines:
                ls = l.split()
                if len(ls) == 2:
                    w = ls[0].strip()
                    GeezScore._all_words[w]=int(ls[1])
                    if  int(ls[1])>100:
                        GeezScore._top_words.add(w)
                    if len(w) in [3,4]:
                        GeezScore._geez_3or4char.add(w)
                        sera = Geez2Sera.geez2sera(w)
                        # if(sera.endswith("E")):
                        #     print(w)
                        if(GeezScore.is_cecece(sera)):
                            GeezScore._geez_cecece.add(w)

                        if(GeezScore.is_caccc(sera)):
                            GeezScore._geez_caccc.add(w)


    @staticmethod
    def exists(word):
        GeezScore.init()
        return GeezScore._all_words[word] if word in GeezScore._all_words else 0

    @staticmethod
    def get3or4char():
        GeezScore.init()
        return GeezScore._geez_3or4char

    @staticmethod
    def get_cecece():
        GeezScore.init()
        return GeezScore._geez_cecece

