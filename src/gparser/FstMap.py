import json
import os
from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
from gparser import TFST
from concurrent.futures import ProcessPoolExecutor, as_completed, wait


class FstMap:
    DIRECTIVES = ['PRESENT', 'PAST', 'VERB2VERB', 'NOUNSUFFIX', 'NOUNPREFIX', 'POSSESSIVE', 'VERB2NOUN', 'VERBSUFFIX',
                  'VERBPREFIX', 'NOUNPLURAL', 'ADJPLURAL', 'ADJPREFIX']
    SRC_DIR = os.path.dirname(__file__)
    map = {}

    def __init__(self):
        f = open(os.path.join(FstMap.SRC_DIR, "FST2.csv"), mode="r", encoding='utf-8')
        lines = f.readlines()
        currentTense = ''
        for line in lines:
            rows = line.split(',')
            if (not rows[0].strip() == ''):
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
                        # FstMap.map[currentTense][rows[0]][object[i]]  = TFST.TFST(feature)
                        FstMap.map[currentTense][rows[0]][object[i]] = feature

    def getMap(self):
        return FstMap.map

    def generate_all2(self, tense, src,simplify=True):
        args = []
        para = {}
        for sub, fsts in FstMap.map[tense].items():
            para[sub] = {}
            for obj, fst in fsts.items():
                para[sub][obj] = {}
                args.append((sub, obj, FstMap.map[tense][sub][obj], src))

        with ProcessPoolExecutor() as executor:
            futures = {executor.submit(FstMap._generate, num[2], num[3]): num for num in args}
        wait(futures)
        for future in as_completed(futures):
            cell = futures[future]
            try:
                result = future.result()
                para[cell[0]][cell[1]] = result
            except Exception as e:
                print(f"Task for {cell} raised an exception: {e}")
        executor.shutdown()
        if ("NOUNPLURAL" in tense and simplify):
            src_geez = Geez2Sera.sera2geez(src)
            plural_para = dict()
            for c, rows in para.items():
                plural_para[c] = {"N": ('', -1)}
                for r, v in rows.items():
                    if (v[1] > plural_para[c]["N"][1] and not src_geez == v[0]):
                        plural_para[c]["N"] = v
            return plural_para
        else:
            return para

    @staticmethod
    def _generate(rule, root):
        fst = TFST.TFST(rule)
        derivative = list(fst.generate(root))[0]
        g_derivative = Geez2Sera.sera2geez(derivative)
        # print(g_derivative)
        # score = 0 if root == derivative else GeezScore.exists(g_derivative)
        score = GeezScore.exists(g_derivative)
        return g_derivative, score


if __name__ == "__main__":
    all_ = FstMap().generate_all2('NOUNPLURAL', "kelIbi")
    print(json.dumps(all_, indent='\t'))
