from src.gparser.FstMap import FstMap
from concurrent.futures import ProcessPoolExecutor, as_completed
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


f = open(file="word_score8K.txt", mode="a", encoding='utf-8', buffering=1)
# f.truncate(0)
def save(counter):
    sorted_counter = dict(sorted(counter.items(), key=lambda item:  -1*item[1] ))
    for s, c in sorted_counter.items():
        geez = Geez2Sera.sera2geez(s)
        store(c,  geez)
    f.close()


def store(geez,cnt):
    # line = "{} {} \n".format(geez, c)
    line = "{} {} {} \n".format(geez, cnt[0], cnt[1])
    f.write(line)
    f.flush()
    os.fsync(f)
    print(line, end="")


def runner(fst, form,root):
    sera = Geez2Sera.geez2sera(root)
    map = fst.generate_all2(form, sera )
    cnt = count_success(map)
    counter[sera] = cnt
    store(root,cnt)


if __name__ == '__main__':

    fst = FstMap()
    os.environ["SCORE_FILE"] = "ti_score.txt"

    counter = {}

    cecece =  ["ነገረ","ከበረ"]
    #cecece =  ["ከልቢ","ድሙ",'ምስራሕ']
    #cecece = GeezScore.get_cecece()
    GeezScore.init()
    cecece = GeezScore._top_words
    print(len(cecece))
    #print(cecece)

    start_time = time.time()
    for x in cecece :
        form = "POSSESSIVE"
        runner(fst,form, x)

    # print(json.dumps(map,indent='\t'))

    print("Elapsed time (seconds):", time.time() - start_time)
