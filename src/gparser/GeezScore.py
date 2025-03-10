import os,re
from gparser.Geez2Sera import Geez2Sera

class GeezScore:
    _all_words = dict()
    _all_const_words = dict()
    score_file = os.path.join(os.path.dirname(__file__), "../resources/ti_score.txt")

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
                    c = Geez2Sera.geez2sera(w).translate('euiaEIo')
                    if( not c in GeezScore._all_const_words):
                        GeezScore._all_const_words[c] = []
                    GeezScore._all_const_words[c].append(w)
                    GeezScore._all_words[w]=int(ls[1])

    @staticmethod
    def exists(word):
        GeezScore.init()
        return GeezScore._all_words[word] if word in GeezScore._all_words else 0


    @staticmethod
    def consonants(word):
        GeezScore.init()
        c = Geez2Sera.geez2sera(word).translate('euiaEIo')
        r = []
        for  x in GeezScore._all_const_words:
            if c in x:
              r = r+  GeezScore._all_const_words[x]
        return r
