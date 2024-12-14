import re
class Geez2Sera:
    _geez_sera = {}
    _sera_geez = {}

    @staticmethod
    def init():
        if len(Geez2Sera._geez_sera) <= 0:
            f = open("sera.txt", encoding='utf-8')
            lines = f.readlines()

            for l in lines:
                ls = l.split(' ')
                if len(ls) == 2:
                    Geez2Sera._geez_sera[ls[0].strip()] = ls[1].strip()
                    Geez2Sera._sera_geez[ls[1].strip()] = ls[0].strip()

    @staticmethod
    def split_syllabus(string):
        # Regular expression to sylobus at every vowel, keeping the vowel with the previous part
        vowels = r'([aeiouEI])'
        syllabus = re.split(vowels, string)
        geez_syllabus = []
        index = -1
        for syl in [x for x in syllabus if len(x.strip()) >= 1]:
            if (re.match(vowels, syl)):
                geez_syllabus[index] = geez_syllabus[index] + syl
            else:

                geez_syllabus.append(syl)
                index = index + 1

        return geez_syllabus

    @staticmethod
    def sera2geez(word):
        Geez2Sera.init()
        words = []
        for w in word.split():
            w3 = "".join([Geez2Sera._sera_geez[w1.strip()] for w1 in Geez2Sera.split_syllabus(w)])
            words.append(w3)

        return " ".join(words)

    @staticmethod
    def geez2sera(word):
        Geez2Sera.init()
        words = []
        for w in word.split():
            w3 = "".join([Geez2Sera._geez_sera[w1] for w1 in w if w1 in Geez2Sera._geez_sera ])
            words.append(w3)

        return " ".join(words)
