
def build_anagram_dict():
    anagram_dict = {}
    with open("words.txt", "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            sorted_word = list(line)
            sorted_word.sort()
            sorted_word = ''.join(sorted_word)
            anagram_dict.setdefault(sorted_word, []).append(line)
    sorted_list = []
    for key in anagram_dict:
        sorted_list.append(anagram_dict[key])
    sorted_list = sorted(sorted_list, key=len, reverse=True)

    with open("anagrams.txt", "w+") as fp:
        for anagram_list in sorted_list:
            fp.write(f'{anagram_list}\n')

    return sorted_list


def find_bingo(sorted_list):
    for anagram_list in sorted_list:
        if len(anagram_list[0]) == 8:
            break
    print(anagram_list)


sorted_list = build_anagram_dict()
find_bingo(sorted_list)
