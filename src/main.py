from src.gparser.FstMap import FstMap
from concurrent.futures import ProcessPoolExecutor, as_completed
from src.gparser.Utils import *
from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
import os

import time




def save(counter):
    f = open(file="word_score8K.txt", mode="w+", encoding='utf-8')
    sorted_counter = dict(sorted(counter.items(), key=lambda item:  -1*item[1] ))
    for geez, c in sorted_counter.items():
        #line = "{} {} \n".format(geez, c)
        line = "{} {} {} \n".format(geez, c[0], c[1])
        f.write(line)
        print(line, end="")
    f.close()


def runner ( form,root):
    fst = FstMap()
    sera = Geez2Sera.geez2sera(root)
    map = fst.generate_all2(form, sera )
    return count_success(map)

def runner3(fst, form,root):
    return 1,2
if __name__ == '__main__':


    os.environ["SCORE_FILE"] = "ti_score.txt"

    counter = {}

    form = "PAST"
    cecece =  ["ነገረ","ከበረ"]
    #cecece =  ["ከልቢ","ድሙ",'ምስራሕ']
    #cecece = GeezScore.get_cecece()
    print(len(cecece))

    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(runner, form,x): x for x in cecece}

    for future in as_completed(futures):
        number = futures[future]
        try:
            result = future.result()
            counter[number]=result
        except Exception as e:
            print(f"Task for {number} raised an exception: {e}")


    save(counter)
    # print(json.dumps(map,indent='\t'))

    print("Elapsed time (seconds):", time.time() - start_time)
