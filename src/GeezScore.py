import os

class GeezScore:
    _geez_score = set()
    _geez_3char = set()

    @staticmethod
    def init():
        if len(GeezScore._geez_score) <= 0 :
            score_file = os.environ["SCORE_FILE"]
            f = open(score_file, encoding='utf-8')
            lines = f.readlines()

            for l in lines:
                ls = l.split()
                if len(ls) == 2:
                    w = ls[0].strip()
                    GeezScore._geez_score.add(w)
                    if len(w) == 3:
                        GeezScore._geez_3char.add(w)

    @staticmethod
    def exists(word):
        GeezScore.init()
        return int(word in GeezScore._geez_score)

    @staticmethod
    def get3char():
        GeezScore.init()
        return GeezScore._geez_3char
