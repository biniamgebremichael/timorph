from src.gparser.FstMap import FstMap
from src.gparser.TFST import TFST
from src.gparser.Utils import *
from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
import os

import time


def consumer(src, x):
    geez = Geez2Sera.sera2geez(x)
    score = GeezScore.exists(geez)
    if(score>0):
        if(not geez in counter[src]):
            counter[src][geez] = 0
        counter[src][geez] =  counter[src][geez] + score
    return geez + '|' + str(score)


def printSingle(word):
    map = fst.generate_all3(["PAST"], Geez2Sera.geez2sera(word), consumer)
    csvPrint(map)


def save(counter):
    f = open(file="word_score2.txt", mode="w+", encoding='utf-8')
    sorted_counter = dict(sorted(counter.items(), key=lambda item: len(item[1])))
    for s, c in sorted_counter.items():
        geez = Geez2Sera.sera2geez(s)
        #line = "{} {} \n".format(geez, c)
        line = "{} {} {} \n".format(geez, len(c), sum([i for i in c.values()] ))
        f.write(line)
        print(line, end="")
    f.close()


def runner(fst, form,sera):
    counter[sera] = {}
    map = fst.generate_all2(form, sera )
    #sera = TFST.generate_passive(sera)
    #counter[sera] = {}
    #map = fst.generate_all3([form], sera, consumer)

    csvPrint(map)
    ##print(sera)


if __name__ == '__main__':

    fst = FstMap()
    os.environ["SCORE_FILE"] = "ti_score.txt"

    counter = {}

    cecece =  ["ሃደመ"]
    #cecece =  ["ከልቢ","ድሙ",'ምስራሕ']
    #cecece = GeezScore.get_cecece()
    print(len(cecece))

    start_time = time.time()
    for x in cecece :
        form = "PAST"
        sera = Geez2Sera.geez2sera(x)
        runner(fst,form, sera)

    save(counter)
    # print(json.dumps(map,indent='\t'))

    print("Elapsed time (seconds):", time.time() - start_time)
