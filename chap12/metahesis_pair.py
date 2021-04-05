word_dict = {}
words_sorted = []

def build_word_dict():
    word_list = []
    with open("words.txt", "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_dict[line.strip()] = -1
            word_list.append(line.strip())
    words = sorted(word_list, key=len, reverse=True)
    word_dict["a"] = 1
    word_dict["i"] = 1
    word_dict[""] = 1
    for word in words:
        words_sorted.append(word)


def check_word(word):
    if word not in word_dict:
        return False
    elif word_dict[word] == 1:
        return True
    elif word_dict[word] == 0:
        return False
    else:
        word_dict[word] = 0
        for i in range(len(word)):
            if check_word(word[:i] + word[i+1:]):
                word_dict[word] = 1
                return True
        return False

def print_subwords(word):
    for i in range(len(word)):
        sub_word = word[:i] + word[i+1:]
        if check_word(sub_word):
            print(word)
            print_subwords(sub_word)
            break

def find_longest_metathesis():
    for word in words_sorted:
        if check_word(word):
            print_subwords(word)
            break


build_word_dict()
find_longest_metathesis()
