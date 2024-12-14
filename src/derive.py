from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
from GeezFst import GeezFst
import sys


def print_all(word_rows):
    total = 0
    for word, rows in word_rows.items():
        print("===",word,"==========")
        for key, values in rows.items():
            if ("OBJECT" in key):
                print(key, end=",\t")
                print(",\t".join(values))
            else:
                print(key, end="\t")
                for v in values:
                    gword = Geez2Sera.sera2geez(v)
                    score = GeezScore.exists(gword)
                    total = total+score
                    print(", " + gword + "+" + str(score), end = "\t")
                print(" ")
    return total


def derive(word):
    fst = GeezFst()
    # word= Geez2Sera.sera2geez(fst.passive(Geez2Sera.geez2sera(word)))
    generated_words, score = fst.generate_all(Geez2Sera.geez2sera(word))
    total_score = print_all(generated_words)
    print(word,total_score)


word = sys.argv[1]
derive(word)
