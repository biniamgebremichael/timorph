import json
from src.parser.Utils import *
from src.parser.TFST import TFST


class FstMap:

    def __init__(self):
        f = open(file="parser/FST2.csv", mode="r", encoding='utf-8')
        lines = f.readlines()
        self.map = {}
        currentTense = ''
        for line in lines:
            rows = line.split(',')
            if (not rows[0].strip() == '' and len(line) > 30):
                if (rows[0].strip() in ['PRESENT', 'PAST','POSSESSIVE']):
                    currentTense = rows[0].strip()
                    self.map[currentTense] = {}
                    object = {}
                    for i in range(1, len(rows)):
                        object[i] = rows[i].strip()
                else:
                    self.map[currentTense][rows[0]] = {}
                    for i in range(1, len(rows)):
                        feature = rows[i].strip()
                        feature = '_' if len(feature) <= 1 else feature
                        self.map[currentTense][rows[0]][object[i]]  = TFST(feature)
                        #self.map[currentTense][rows[0]][object[i]] =  feature

    def getMap(self):
        return self.map

    def generate_all(self, src):
        return {tense: {sub: {obj: list(fst.generate(src))[0] for obj, fst in fsts.items() if not fst.isEmpty()} for
                        sub, fsts in value.items()} for tense, value in self.map.items()}



    def generate_all3(self,tenses, src,consume):
        return {tense: {sub: {obj: consume(src,list(fst.generate(src))[0]) for obj, fst in fsts.items() if not fst.isEmpty()} for
                        sub, fsts in self.map[tense].items()} for tense  in tenses}
if __name__ == "__main__":

    print(json.dumps(FstMap().getMap(), indent='\t'))


    for x,y in FstMap().getMap().items():
        header = x+','+','.join([a for a,b in  y['I'].items()])
        print(header)
        for a,b in y.items():
            line = a + ',' + ','.join([m.replace("I",'') for n, m in y[a].items()])
            print(line)


# print(json.dumps(FstMap().generate_all('negere'),indent='\t'))
