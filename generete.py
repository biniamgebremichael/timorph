from pyfoma import FST

variable = {'V': FST.re("[aeiouI@E]"),
            'C': FST.re("[bcdfghjklmnpqrstvwxyz12HQKNZCPSQW]"),
            "empty": FST.re("$^rewrite(a:a)"),
            "6e_u": FST.re("$^rewrite((e):u /  _ #,longest = True, leftmost = True  )"),
            "6e_o": FST.re("$^rewrite((e):o /  _ #,longest = True, leftmost = True  )"),
            "6e_om": FST.re("$^rewrite((e):(om) /  _ #,longest = True, leftmost = True  )"),
            "6e_ka": FST.re("$^rewrite((e):(ka) /   _ # ,longest = True, leftmost = True )"),
            "6e_ki": FST.re("$^rewrite((e):(ki) /   _ # ,longest = True, leftmost = True  )"),
            "6_t": FST.re("$^rewrite('':(t) / _ #, longest = True, leftmost = True  )"),
            "6_n": FST.re("$^rewrite('':n / _  #, longest = True, leftmost = True )"),
            "6_na": FST.re("$^rewrite('':(na) / e  _  #, longest = True, leftmost = True )"),
            "6e_a": FST.re("$^rewrite(e:(a) / _ #, longest = True, leftmost = True  )"),
            "6e_kum": FST.re("$^rewrite(e:(kum) /   _  #,longest = True, leftmost = True )"),
            "6e_kn": FST.re("$^rewrite(e:(kn) / _ #,longest = True, leftmost = True  )"),
            "_ni": FST.re("$^rewrite('':(ni)  / _  #,longest = True, leftmost = True ) "),
            "n_nani": FST.re("$^rewrite('':(ani)  / n _  #,longest = True, leftmost = True ) "),
            "_tni": FST.re("$^rewrite('':(tni)  / _  #,longest = True, leftmost = True ) "),
            "i_ni": FST.re("$^rewrite('i':(ni)  / ki _  #,longest = True, leftmost = True ) "),
            "_yo": FST.re("$^rewrite('':(yo) / _  #,longest = True, leftmost = True ) "),
            "_to": FST.re("$^rewrite('':(to) / _  #,longest = True, leftmost = True ) "),
            "_wo": FST.re("$^rewrite('':(wo) / _  #,longest = True, leftmost = True ) "),
            "_1o": FST.re("$^rewrite('':(1o) / _  #,longest = True, leftmost = True ) "),
            "_mo": FST.re("$^rewrite('':(mo) / _  #,longest = True, leftmost = True ) "),
            "_o": FST.re("$^rewrite('':(o) / _  #,longest = True, leftmost = True ) "),
            "_ya": FST.re("$^rewrite('':(ya) / _  #,longest = True, leftmost = True ) "),
            "_ta": FST.re("$^rewrite('':(ta) / _  #,longest = True, leftmost = True ) "),
            "_wa": FST.re("$^rewrite('':(wa) / _  #,longest = True, leftmost = True ) "),
            "_1a": FST.re("$^rewrite('':(1a) / _  #,longest = True, leftmost = True ) "),
            "_ma": FST.re("$^rewrite('':(ma) / _  #,longest = True, leftmost = True ) "),
            "_a": FST.re("$^rewrite('':(a) / _  #,longest = True, leftmost = True ) ")
            }

variable["4e_i"] = FST.re("$^rewrite((e):i /$C$V$C _ $C$V ,longest = True, leftmost = True )", variable)
variable["4e_a"]: FST.re("$^rewrite((e):a /$C$V$C _ $C$V ,longest = True, leftmost = True  ) ", variable)


def passive(word):
    fst = FST.re(" $^rewrite(($V?):'' / # $C _  ) @ $^rewrite((''):(1a) / # _   ) ", variable)
    return   list(fst.generate(word))[0]


def ccc_verbs():
    fsts = {}
    fsts["PRE"] = {}
    fsts["PAS"] = {}
    fsts["PRE"]["N"] = {}
    fsts["PAS"]["N"] = {}
    fsts["PRE"]["N"]["I"] = variable['4e_i']
    fsts["PAS"]["N"]["I"] = variable["4e_i"]
    fsts["PRE"]["N"]["HE"] = variable["empty"]
    fsts["PAS"]["N"]["HE"] = FST.re("$4e_i @ $6e_u", variable)
    fsts["PRE"]["N"]["SHE"] = variable["6_t"]
    fsts["PAS"]["N"]["SHE"] = FST.re("$4e_i @ $6e_a", variable)
    fsts["PRE"]["N"]["WE"] = variable["6_na"]
    fsts["PAS"]["N"]["WE"] = FST.re("$4e_i @ $6_na", variable)
    fsts["PRE"]["N"]["THEY_M"] = variable["6e_u"]
    fsts["PAS"]["N"]["THEY_M"] = FST.re("$4e_i @ $6e_om", variable)
    fsts["PRE"]["N"]["THEY_F"] = variable["6e_a"]
    fsts["PAS"]["N"]["THEY_F"] = FST.re("$4e_i @ $6_n", variable)
    fsts["PRE"]["N"]["YOU_SM"] = variable["6e_ka"]
    fsts["PAS"]["N"]["YOU_SM"] = FST.re("$4e_i @ $6e_ka", variable)
    fsts["PRE"]["N"]["YOU_SF"] = variable["6e_ki"]
    fsts["PAS"]["N"]["YOU_SF"] = FST.re("$4e_i @ $6e_ki", variable)
    fsts["PRE"]["N"]["YOU_PM"] = variable["6e_kum"]
    fsts["PAS"]["N"]["YOU_PM"] = FST.re("$4e_i @ $6e_kum", variable)
    fsts["PRE"]["N"]["YOU_PF"] = variable["6e_kn"]
    fsts["PAS"]["N"]["YOU_PF"] = FST.re("$4e_i @ $6e_kn", variable)

    fsts["PRE"]["ME"] = {}
    fsts["PAS"]["ME"] = {}
    fsts["PRE"]["ME"]["I"] = variable["4e_i"]
    fsts["PAS"]["ME"]["I"] = variable["4e_i"]
    fsts["PRE"]["ME"]["HE"] = variable["_ni"]
    fsts["PAS"]["ME"]["HE"] = FST.re("$4e_i @ $6e_u @ $_ni", variable)
    fsts["PRE"]["ME"]["SHE"] = FST.re("$6_t @ $_ni", variable)
    fsts["PAS"]["ME"]["SHE"] = FST.re("$4e_i @ $6e_a  @ $_tni", variable)
    fsts["PRE"]["ME"]["WE"] = FST.re("$6_na  ", variable)
    fsts["PAS"]["ME"]["WE"] = FST.re("$4e_i @ $6_na  ", variable)
    fsts["PRE"]["ME"]["THEY_M"] = FST.re("$6e_u @ $_ni", variable)
    fsts["PAS"]["ME"]["THEY_M"] = FST.re("$4e_i @ $6e_om @ $_ni", variable)
    fsts["PRE"]["ME"]["THEY_F"] = FST.re("$6e_a @ $_ni", variable)
    fsts["PAS"]["ME"]["THEY_F"] = FST.re("$4e_i @ $6_na @ $_ni", variable)
    fsts["PRE"]["ME"]["YOU_SM"] = FST.re("$6e_ka  @ $_ni", variable)
    fsts["PAS"]["ME"]["YOU_SM"] = FST.re("$4e_i @ $6e_ka  @ $_ni", variable)
    fsts["PRE"]["ME"]["YOU_SF"] = FST.re("$6e_ki @ $i_ni", variable)
    fsts["PAS"]["ME"]["YOU_SF"] = FST.re("$4e_i @ $6e_ki @ $i_ni", variable)
    fsts["PRE"]["ME"]["YOU_PM"] = FST.re("$6e_kum @ $_ni", variable)
    fsts["PAS"]["ME"]["YOU_PM"] = FST.re("$4e_i @ $6e_kum @ $_ni", variable)
    fsts["PRE"]["ME"]["YOU_PF"] = FST.re("$6e_kn @ $n_nani", variable)
    fsts["PAS"]["ME"]["YOU_PF"] = FST.re("$4e_i @ $6e_kn @ $n_nani", variable)

    fsts["PRE"]["HER"] = {}
    fsts["PAS"]["HER"] = {}
    fsts["PRE"]["HER"]["I"] = FST.re("$4e_i @ $_ya", variable)
    fsts["PAS"]["HER"]["I"] = FST.re("$4e_i @ $_ya", variable)
    fsts["PRE"]["HER"]["HE"] = FST.re("$6e_a", variable)
    fsts["PAS"]["HER"]["HE"] = FST.re("$4e_i @ $6e_u @ $_wa", variable)
    fsts["PRE"]["HER"]["SHE"] = FST.re("$6_t @ $_a", variable)
    fsts["PAS"]["HER"]["SHE"] = FST.re("$4e_i @ $6e_a  @ $_ta", variable)
    fsts["PRE"]["HER"]["WE"] = FST.re("$6_na @ $_ya", variable)
    fsts["PAS"]["HER"]["WE"] = FST.re("$4e_i @ $6_na @ $_ya", variable)
    fsts["PRE"]["HER"]["THEY_M"] = FST.re("$6e_u @ $_wa", variable)
    fsts["PAS"]["HER"]["THEY_M"] = FST.re("$4e_i @ $6e_om @ $_wa", variable)
    fsts["PRE"]["HER"]["THEY_F"] = FST.re("$6e_a @ $_1a", variable)
    fsts["PAS"]["HER"]["THEY_F"] = FST.re("$4e_i @ $6_n @ $_1a", variable)
    fsts["PRE"]["HER"]["YOU_SM"] = FST.re("$6e_ka  @ $_ya", variable)
    fsts["PAS"]["HER"]["YOU_SM"] = FST.re("$4e_i @ $6e_ka  @ $_ya", variable)
    fsts["PRE"]["HER"]["YOU_SF"] = FST.re("$6e_ki @ $_ya", variable)
    fsts["PAS"]["HER"]["YOU_SF"] = FST.re("$4e_i @ $6e_ki @ $_ya", variable)
    fsts["PRE"]["HER"]["YOU_PM"] = FST.re("$6e_kum @ $_wa", variable)
    fsts["PAS"]["HER"]["YOU_PM"] = FST.re("$4e_i @ $6e_kum @ $_wa", variable)
    fsts["PRE"]["HER"]["YOU_PF"] = FST.re("$6e_kn @ $_1a", variable)
    fsts["PAS"]["HER"]["YOU_PF"] = FST.re("$4e_i @ $6e_kn @ $_1a", variable)

    fsts["PRE"]["HIM"] = {}
    fsts["PAS"]["HIM"] = {}
    fsts["PRE"]["HIM"]["I"] = FST.re("$4e_i @ $_yo", variable)
    fsts["PAS"]["HIM"]["I"] = FST.re("$4e_i @ $_yo", variable)
    fsts["PRE"]["HIM"]["HE"] = FST.re("$6e_o", variable)
    fsts["PAS"]["HIM"]["HE"] = FST.re("$4e_i @ $6e_u @ $_wo", variable)
    fsts["PRE"]["HIM"]["SHE"] = FST.re("$6_t @ $_o", variable)
    fsts["PAS"]["HIM"]["SHE"] = FST.re("$4e_i @ $6e_a  @ $_to", variable)
    fsts["PRE"]["HIM"]["WE"] = FST.re("$6_na @ $_yo", variable)
    fsts["PAS"]["HIM"]["WE"] = FST.re("$4e_i @ $6_na @ $_yo", variable)
    fsts["PRE"]["HIM"]["THEY_M"] = FST.re("$6e_u @ $_wo", variable)
    fsts["PAS"]["HIM"]["THEY_M"] = FST.re("$4e_i @ $6e_om @ $_wo", variable)
    fsts["PRE"]["HIM"]["THEY_F"] = FST.re("$6e_a @ $_1o", variable)
    fsts["PAS"]["HIM"]["THEY_F"] = FST.re("$4e_i @ $6_n @ $_1o", variable)
    fsts["PRE"]["HIM"]["YOU_SM"] = FST.re("$6e_ka  @ $_yo", variable)
    fsts["PAS"]["HIM"]["YOU_SM"] = FST.re("$4e_i @ $6e_ka  @ $_yo", variable)
    fsts["PRE"]["HIM"]["YOU_SF"] = FST.re("$6e_ki @ $_yo", variable)
    fsts["PAS"]["HIM"]["YOU_SF"] = FST.re("$4e_i @ $6e_ki @ $_yo", variable)
    fsts["PRE"]["HIM"]["YOU_PM"] = FST.re("$6e_kum @ $_wo", variable)
    fsts["PAS"]["HIM"]["YOU_PM"] = FST.re("$4e_i @ $6e_kum @ $_wo", variable)
    fsts["PRE"]["HIM"]["YOU_PF"] = FST.re("$6e_kn @ $_1o", variable)
    fsts["PAS"]["HIM"]["YOU_PF"] = FST.re("$4e_i @ $6e_kn @ $_1o", variable)

    return fsts



def print_all(word_rows,english_word):
    for word, rows in word_rows.items():
        print("==========")
        sera = sera2geez(None,word)
        print(sera)
        for tense, subjects in rows.items():
            print(tense)
            for key, values in subjects.items():
                print(key, end=",")
                if("OBJECT" in key):
                    print(",\t".join(values))
                else:
                    print(",\t".join([sera2geez(None,v) + " ("+key + " "+english_word+" " + subjects["OBJECT"][index]  +") " for index,v in enumerate(values)]))


def generate_all(fsts, words):
    word_rows = {}
    for word in words:
        word_rows[word] = {}
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
                    row[subject].append(result_pre)
            word_rows[word][tense] = row
    return word_rows


def main(word,english):

    word_active = geez2sera(None, word)
    word_passive = passive(word_active)
    ccc_fsts = ccc_verbs()
    generated_words = generate_all(ccc_fsts, [word_active, word_passive])
    print_all(generated_words,english)

word_active = "ሓጸበ"
english_meaning  = "wash"
main(word_active,english_meaning)
