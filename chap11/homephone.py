from pronounce import read_dictionary

def build_dictionary():
    word_dict = dict()
    with open("words.txt", 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_dict[line.strip()] = None

    return word_dict

def find_words(word_dict):
    found_words = dict()
    with open("words.txt") as fp:
        while True:
            lin = fp.readline()
            if not lin:
                break
            line = lin.strip()
            if len(line) == 5:
                s1 = line[1:]
                s2 = line[0] + line[2:]
                if s1 in word_dict and s2 in word_dict:
                    found_words[line] = [s1, s2]
    return found_words

def check_pronunciation(found_words, pro_dict):
    for key in found_words:
        word1 = found_words[key][0]
        word2 = found_words[key][1]
        if key in pro_dict and word1 in pro_dict and word2 in pro_dict:
            # print(pro_dict[key])
            # print(pro_dict[key])
            # print(pro_dict[key])
            if pro_dict[key] == pro_dict[word1] and pro_dict[key] == pro_dict[word2]:
                print(f"{key} {word1} {word2}\n")


word_dict = build_dictionary()
found_words = find_words(word_dict)
pro_dict = read_dictionary()
check_pronunciation(found_words, pro_dict)
