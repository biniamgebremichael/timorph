import json
import os
from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
from  gparser  import TFST
from concurrent.futures import ProcessPoolExecutor, as_completed

class FstMap:

    DIRECTIVES = ['PRESENT', 'PAST', 'POSSESSIVE','SUFFIX','PREFIX','PASSIVE','VERB2NOUN']
    SRC_DIR =  os.path.dirname(__file__)
    map = {}
    executor = ProcessPoolExecutor(max_workers=50)
    def __init__(self):
        f = open(os.path.join(FstMap.SRC_DIR, "FST2.csv"), mode="r", encoding='utf-8')
        lines = f.readlines() 
        currentTense = ''
        for line in lines:
            rows = line.split(',')
            if (not rows[0].strip() == ''  ):
                if (rows[0].strip() in FstMap.DIRECTIVES):
                    currentTense = rows[0].strip()
                    FstMap.map[currentTense] = {}
                    object = {}
                    for i in range(1, len(rows)):
                        object[i] = rows[i].strip()
                else:
                    FstMap.map[currentTense][rows[0]] = {}
                    for i in range(1, len(rows)):
                        feature = rows[i].strip()
                        feature = '_' if len(feature) <= 1 else feature
                        #FstMap.map[currentTense][rows[0]][object[i]]  = TFST.TFST(feature)
                        FstMap.map[currentTense][rows[0]][object[i]] =  feature

    def getMap(self):
        return FstMap.map


    def generate_all2(self, tense, src):
        args = []
        para = {}
        for sub, fsts in FstMap.map[tense].items():
            para[sub] = {}
            for obj, fst in fsts.items():
                para[sub][obj]={}
                args.append((sub,obj,FstMap.map[tense][sub][obj],src))

        with ProcessPoolExecutor() as executor:
            futures = {executor.submit(FstMap._generate,num[2],num[3]): num for num in args}

        for future in as_completed(futures):
            number = futures[future]
            try:
                result = future.result()
                para[number[0]][number[1]]=result
            except Exception as e:
                print(f"Task for {number} raised an exception: {e}")
        #print(json.dumps(para, indent='\t'))
        return para

    @staticmethod
    def _generate(rule,root):
          fst = TFST.TFST(rule)
          derivative = list(fst.generate(root))[0]
          g_derivative = Geez2Sera.sera2geez(derivative)
          score = GeezScore.exists(g_derivative)
          return g_derivative,score



if __name__ == "__main__":
    os.environ["SCORE_FILE"] = "ti_score.txt"
    #print(json.dumps(FstMap().getMap()['SUFFIX'] , indent='\t'))
    print(json.dumps(FstMap().generate_all2('SUFFIX',"hademe"), indent='\t'))


