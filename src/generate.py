import json,os,sys
from concurrent.futures import ThreadPoolExecutor
from Geez2Sera import Geez2Sera
from GeezScore import GeezScore
from GeezFst import GeezFst


def print_all(word_rows, english_word):
    for word, rows in word_rows.items():
        print("==========")
        for tense, subjects in rows.items():
            print(tense)
            for key, values in subjects.items():
                print(key, end=",")
                if ("OBJECT" in key):
                    print(",\t".join(values))
                else:
                    eng = [" (" + key + " " + english_word + " " + subjects["OBJECT"][index] + ") " for index, v in
                           enumerate(values)]
                    print(",\t".join(
                        [Geez2Sera.sera2geez(v) + "+" + str(GeezScore.exists(Geez2Sera.sera2geez(v))) for index, v in
                         enumerate(values)]))
                    # print(sum([Score.exists(Geez2Sera.sera2geez(v))  for v in values]), '/', len(values))
                    # print(",\t".join(values))
                    # print(",\t".join([Geez2Sera.sera2geez( v) + eng[index] for index,v in enumerate(values)]))


def generate_all(fsts, word):
    word_rows = {}
    score = 0
    total = 0
    for tense in fsts:
        row = {}
        row['OBJECT'] = []
        for object in fsts[tense]:
            row['OBJECT'].append(object)
            for subject in fsts[tense][object]:
                p = fsts[tense][object][subject]
                if not subject in row:
                    row[subject] = []
                result_pre = list(p.generate(word))[0]
                score += GeezScore.exists(Geez2Sera.sera2geez(result_pre))
                total += 1
                row[subject].append(result_pre)
        word_rows[tense] = row
    return word_rows, int((score * 100) / total)


scorelist = dict()


def generate(ccc_fsts, word):
    generated_words, score = generate_all(ccc_fsts, word)
    print(end='.')
    #print(Geez2Sera.sera2geez(word), str(score) + "%")
    scorelist[Geez2Sera.sera2geez(word)] = score
    # print_all({word:generated_words},  '')


def main(word):
    sft = GeezFst()
    word_active = Geez2Sera.geez2sera(word)
    ccc_fsts = sft.ccc_verbs()
    generate(ccc_fsts, word_active)
    generate(ccc_fsts, sft.passive(word_active))


# test7()
os.environ['SCORE_FILE'] = sys.argv[1]
words = ["ተቐበለ", "ሓጸበ", 'ሰበረ', 'ደንገጸ', 'ሳዕስዐ']
#words = GeezScore.get3char()
executor = ThreadPoolExecutor()
for word in words:
    executor.submit(main, word )

executor.shutdown()
f = open(file="word_score.txt", mode="w", encoding='utf-8')
for x in scorelist:
    f.write(x)
    f.write("\t")
    f.write(str(scorelist[x]))
    f.write('\n')
f.flush()
f.close()
