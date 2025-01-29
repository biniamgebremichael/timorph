import re ,os


def _add_vowel_I(input_str):
    # Define patterns for consonants and vowels
    consonant_pattern = r"[bcdfghjklmnpqrstvwxyz12HQKNZCPSQWAO]"
    vowel_pattern = r"[aeiouIE]"

    # Initialize result list
    result = []
    is_previous_vowel = None  # Tracks whether the previous character was a vowel

    for char in input_str:
        if re.fullmatch(consonant_pattern, char):
            current_is_vowel = False
        elif re.fullmatch(vowel_pattern, char):
            current_is_vowel = True
        else:
            # Non-alphabetic characters are ignored
            result.append(char)
            continue

        # Check alternation
        if is_previous_vowel is not None and is_previous_vowel == current_is_vowel:
            # Add 'i' if alternation rule is broken
            result.append('I')
            is_previous_vowel = not is_previous_vowel  # Alternate manually

        # Append the current character
        result.append(char)
        is_previous_vowel = current_is_vowel

    if re.fullmatch(consonant_pattern, result[len(result) - 1]):
        result.append('I')

    return ''.join(result)


def validate(src):
    if ("@" in src):
        return " @ ".join([_validate(s) for s in src.split("@")])
    else:
        return _validate(src)


def _validate(src):
    pattern = "^(\-){0,1}(\d){0,1}(\\$*[aeiouIEV]*)_(\w*)$"
    if (re.match(pattern, src.strip())):
        (d, p, f, t) = re.match(pattern, src.strip()).groups()
        t = _add_vowel_I(t)
        if ((f is None or not re.match("[aeiouE]", f)) and (not t is None and re.match("[aeiouIE]", t[0]))):
            print('why replace vowel', src)

        if not f is None and re.match("[aeiouE]", f) and not t is None and not re.match("[aeiouIE]", t[0]):
            print('It should replace a vowel', src)
            t = 'I' + t
        src = (d if d else '') + (p if p else '') + (f if f else '') + "_" + t
    else:
        print('not valid', src)
    return src


def count_success(maps):
    unique= set()
    count = 0
    for x in maps:
        for y in maps[x]:
            if(maps[x][y][1]):
                count= count+1
                unique.add(maps[x][y][0])
    return count,len(unique)

def csvPrint(map):
    for x, y in map.items():
        header = f"{x:<{15}}" + ',' + ','.join([f"{a:<{15}}"  for a in y['N']])
        print(header)
        for a, b in y.items():
            line = f"{a:<{15}}" + ',' + ','.join([f"{m:<{15}}"  for m in y[a] ])
            print(line)

def getNouns():
    return getInput("nouns.txt","N")
def getVerbs():
    return getInput("verbs.txt","V")
def getInput(pos_file,posid):
    score_file = os.path.join(os.path.dirname(__file__),  f"../resources/{pos_file}")
    f = open(score_file, encoding='utf-8')
    lines = f.readlines()
    return [(l.strip(),posid ) for l in lines]

def csvPrint2(base, form, map):
    for x, y in map.items():
        for a, b in y.items():
            if(len(list(y[a]) )>0):
                line = f"{base:<{15}}, {form:<{15}} ,  {x:<{15}} , {a:<{15}} , " +  ','.join([f"{m:<{15}}"  for m in y[a] ])
                print(line)
