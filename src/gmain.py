from gparser.FstMap import FstMap
from gparser.Utils import *
from Geez2Sera import Geez2Sera
from persist.Germination import Germination
from persist.DbPersist import DbPersistor
from concurrent.futures import ProcessPoolExecutor, as_completed

import time

from functools import lru_cache


@lru_cache(maxsize=20)
def runner(form, root):
    fst = FstMap()
    sera = Geez2Sera.geez2sera(root)
    map = fst.generate_all2(form, sera)
    return map
    # cnt = count_success(map)
    # counter[sera] = cnt
    # store(root, json.dumps({"map":map}))


def runOnBaseTense(parentroot, word, pos, base_tense, forms):
    dbPersistor = DbPersistor()
    if (base_tense in forms[pos]):
        for feature in forms[pos][base_tense]:
            if (dbPersistor.existGermination(word, pos, base_tense, feature) <= 0):
                map = runner(feature, word)
                map_ = [x.to_tuple() for x in Germination.objectify(parentroot, word, base_tense, pos, feature, map)]
                dbPersistor.addGermination(map_)
                csvPrint2(word, base_tense + "_" + feature, map)
            else:
                print(word, pos, base_tense, '>', feature, 'already done')


if __name__ == '__main__':

    fst = FstMap()

    cecece = getVerbs()
    forms = {
        "V":
            {
                "ROOT": ["PRESENT", "PAST", "VERBPREFIX", "VERBSUFFIX", "VERB2VERB", "VERB2NOUN"],
                "PRESENT": ["VERBPREFIX", "VERBSUFFIX", "VERB2VERB"],
                "PAST": ["VERBPREFIX", "VERBSUFFIX", "VERB2VERB"],
                "VERBPREFIX": ["VERBSUFFIX"],
                "VERB2VERB": ["VERBSUFFIX"],
                "VERB2NOUN": ["POSSESSIVE", "NOUNSUFFIX", "NOUNPREFIX"],
            },
        "N":
            {"ROOT": ["POSSESSIVE", "NOUNPLURAL", "NOUNSUFFIX", "NOUNPREFIX"],
             },
        "A": {"ROOT": ["ADJPLURAL", "ADJPREFIX"]}
    }
    dbPersistor = DbPersistor()
    start_time = time.time()

    futures = {}
    with ProcessPoolExecutor(max_workers=5) as executor:
        for c in cecece:
            futures[executor.submit(runOnBaseTense, c[0], c[0], c[1], c[2], forms)] = c
    for future in as_completed(futures):
        future.result()

    futures = {}
    germs = dbPersistor.getGerminations()
    with ProcessPoolExecutor(max_workers=5) as executor:
        for germ in germs:
            futures[executor.submit(runOnBaseTense, germ.parent, germ.germinated, germ.pos, germ.feature, forms)] = germ

    for future in as_completed(futures):
        future.result()
    print("Elapsed time (seconds):", time.time() - start_time)
