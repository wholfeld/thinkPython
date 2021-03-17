def rotate_pairs():
    word_dict = dict()
    rotated_dict = dict()
    with open("words.txt", "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_dict[line.strip()] = None

    with open("words.txt", "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            sorted_list = get_sorted_rotated_words(line.strip())
            key = None
            word_list = []
            for word in sorted_list:
                if word in word_dict and not key:
                    key = word
                elif word in word_dict:
                    word_list.append(word)
            if key not in rotated_dict and len(word_list) > 0:
                rotated_dict[key] = word_list

    with open("RotatedList.txt", "w+") as wp:
        for key in rotated_dict:
            wp.write(f'{key} : {rotated_dict[key]}\n')


def get_sorted_rotated_words(word):
    words_list = []
    for i in range(len(word)):
        words_list.append(word[i:] + word[:i])

    words_list.sort()

    return words_list


rotate_pairs()