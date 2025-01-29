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


def runOnBaseTense2(parentroot, word, pos, base_tense, forms):
    dbPersistor = DbPersistor()
    for feature in forms:
        if (dbPersistor.existGermination(word, pos, base_tense, feature) <= 0):
            map = runner(feature, word)
            map_ = [x.to_tuple() for x in Germination.objectify(parentroot, word, base_tense, pos, feature, map)]
            dbPersistor.addGermination(map_)
            csvPrint2(word, base_tense + "_" + feature, map)
        else:
            print(word, pos, base_tense, '>', feature, 'already done')


def runOnBaseTense(parentroot,short_path,long_path, word, pos, base_tense, forms):
    dbPersistor = DbPersistor()
    if (base_tense in forms[pos]):
        for feature in forms[pos][base_tense]:
            if (dbPersistor.existGermination(word, pos,  short_path, feature) <= 0):
                map = runner(feature, word)
                map_ = [x.to_tuple() for x in Germination.objectify(parentroot,short_path,long_path, word,  pos, feature, map)]
                dbPersistor.addGermination(map_)
                print(".",end='') #csvPrint2(word, parentbase + "_" + feature, map)
            else:
                print(word, pos, base_tense, '>', feature, 'already done')


def run(germs):
    futures = {}
    with ProcessPoolExecutor(max_workers=5) as executor:
        for germ in germs:
            short_path = germ.feature if germ.feature=="ROOT" else germ.shortpath + '.' + germ.feature
            long_path = germ.feature if germ.feature=="ROOT" else germ.longpath + '.' + germ.feature + '-' + germ.subject + '+' + germ.object
            futures[executor.submit(runOnBaseTense, germ.parent, short_path,long_path, germ.germinated, germ.pos, germ.feature,
                                    forms)] = germ
    for future in as_completed(futures):
        future.result()


if __name__ == '__main__':

    fst = FstMap()

    #cecece = [Germination.rootGermination("ሓተተ","V")]
    cecece = [Germination.rootGermination(x[0],x[1]) for x in getVerbs()[0:10]]
    forms = {
        "V":
            {
                "ROOT": ["PAST", "PRESENT", "VERBPREFIXPAST", "VERBSUFFIX", "PASSIVE", "VERB2NOUN","VERBY"],
                "PAST": ["VERBPREFIXPAST", "VERBSUFFIX" ],
                "VERBY": ["VERBPREFIXPAST", "VERBSUFFIX" ],
                "PRESENT": ["VERBPREFIXPRESENT", "VERBSUFFIX" ],
                "VERBPREFIXPAST": ["VERBSUFFIX"],
                "VERBPREFIXPRESENT": ["VERBSUFFIX"],
                "VERB2NOUN": ["POSSESSIVE", "NOUNSUFFIX", "NOUNPREFIX"],
            },
        "N":
            {"ROOT": ["POSSESSIVE", "NOUNPLURAL", "NOUNSUFFIX", "NOUNPREFIX"],
             },
        "A": {"ROOT": ["ADJPLURAL", "ADJPREFIX"]}
    }
    dbPersistor = DbPersistor()
    start_time = time.time()
    run(cecece)
    run(dbPersistor.getGerminations())
    run(dbPersistor.getGerminations())

    time_start_time = time.time() - start_time
    print("Elapsed time ", time_start_time, 'sec - ', time_start_time/60, 'min - ', time_start_time/3600, 'hrs - ')
