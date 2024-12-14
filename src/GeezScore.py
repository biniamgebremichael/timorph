import os,re
from Geez2Sera import Geez2Sera

class GeezScore:
    _all_words = set()
    _geez_3or4char = set()
    _geez_cecece = set()

    @staticmethod
    def is_cecece(word):
        # Define a regex pattern for consonant-vowel-consonant-vowel-consonant-vowel
        pattern = r'^[^aeiouIE][\w][^aeiouIE][\w][^aeiouIE][\w]$'
        return bool(re.fullmatch(pattern, word))

    @staticmethod
    def init():
        if len(GeezScore._all_words) <= 0 :
            score_file = os.environ["SCORE_FILE"]
            f = open(score_file, encoding='utf-8')
            lines = f.readlines()

            for l in lines:
                ls = l.split()
                if len(ls) == 2:
                    w = ls[0].strip()
                    GeezScore._all_words.add(w)
                    if len(w) in [3,4]:
                        GeezScore._geez_3or4char.add(w)
                        sera = Geez2Sera.geez2sera(w)
                        if(GeezScore.is_cecece(sera)):
                            GeezScore._geez_cecece.add(w)


    @staticmethod
    def exists(word):
        GeezScore.init()
        return int(word in GeezScore._all_words)

    @staticmethod
    def get3or4char():
        GeezScore.init()
        return GeezScore._geez_3or4char

    @staticmethod
    def get_cecece():
        GeezScore.init()
        return GeezScore._geez_cecece

