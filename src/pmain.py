

from gparser.FstMap import FstMap
from concurrent.futures import ProcessPoolExecutor, as_completed
from gparser.Utils import *
from gparser.Geez2Sera import Geez2Sera
from gparser.GeezScore import GeezScore
import os

import time

f = open(file="word_score8K.txt", mode="a", encoding='utf-8', buffering=1)
def store(geez,cnt):
    # line = "{} {} \n".format(geez, c)
    line = "{} {} {} \n".format(geez, cnt[0], cnt[1])
    f.write(line)
    f.flush()
    os.fsync(f)
    print(line, end="")


def runner( form,root):
    fst = FstMap()
    sera = Geez2Sera.geez2sera(root)
    map = fst.generate_all2(form, sera )
    cnt = count_success(map)
    #counter[sera] = cnt
    store(root,cnt)
    return cnt


if __name__ == '__main__':

    os.environ["SCORE_FILE"] = "ti_score.txt"

    progress= 0

    form = "POSSESSIVE"
    #cecece =  ["ነገረ","ከበረ"]
    cecece =  ["ከልቢ","ድሙ",'ምስራሕ']
    #cecece = GeezScore.get_cecece()
    GeezScore.init()
    cecece = list(GeezScore._top_words)[0:100]
    size = len(cecece)
    print(size)
    #print(cecece)

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(runner,form,x): x for x in cecece}

    for future in as_completed(futures):
        input = futures[future]
        try:
            result = future.result()
            print("{}%: {} {}",(100*progress//size),input ,result)
        except Exception as e:
            print(f"Task for {input} raised an exception: {e}")

    print("Elapsed time (seconds):", time.time() - start_time)
