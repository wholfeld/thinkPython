import timeit

def build_word_list():
    word_list = []
    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_list.append(line.strip())
    return word_list

def bisect_search_itr(word_list, search_word):
    left_idx = 0
    right_idx = len(word_list)
    while left_idx < right_idx:
        mid = left_idx // 2 + right_idx // 2
        if search_word > word_list[mid]:
            left_idx = mid + 1
        elif search_word < word_list[mid]:
            right_idx = mid - 1
        else:
            return True
    return False

def bisect_search_recursive(word_list, search_word, left_itr, right_itr):
    if left_itr >= right_itr:
        return False
    mid = left_itr //2 + right_itr // 2
    if word_list[mid] == search_word:
        return True
    elif search_word < word_list[mid]:
        return bisect_search_recursive(word_list, search_word, left_itr, mid - 1)
    else:
        return bisect_search_recursive(word_list, search_word, mid + 1, right_itr)



def runtime(func_name, f):
    start = timeit.default_timer()
    f()
    stop = timeit.default_timer()
    print(f'your function {func_name} took {stop - start} to run.\n')


def runtime_itr():
    start = timeit.default_timer()

    print(bisect_search_itr(word_list, 'aal'))
    print(bisect_search_itr(word_list, 'aa'))
    print(bisect_search_itr(word_list, 'zymurgy'))

    print(bisect_search_itr(word_list, 'aarg'))

    stop = timeit.default_timer()
    print(f'your function iterative took {stop - start} to run.\n')

def runtime_recursive():
    start = timeit.default_timer()

    print(bisect_search_recursive(word_list, 'aal', 0, words_len))
    print(bisect_search_recursive(word_list, 'aa', 0, words_len))
    print(bisect_search_recursive(word_list, 'zymurgy', 0, words_len))
    print(bisect_search_recursive(word_list, 'aarg', 0, words_len))

    stop = timeit.default_timer()
    print(f'your function recurvive took {stop - start} to run.\n')

def reverse_string(word):
    return word[::-1]

def reverse_pairs(word_list):
    file = open("reversed.txt", 'w+')
    for word in word_list:
        reverse_str = reverse_string(word)
        if word != reverse_str and bisect_search_itr(word_list, reverse_str):
            if word < reverse_str:
                file.write(f'{word} : {reverse_str}\n')

def interlock_two(word_list):
    file = open("interlock_twos.txt", 'w+')
    for word in word_list:
        if len(word) > 1:
            f_word = word[::2]
            s_word = word[1::2]
            if bisect_search_itr(word_list, f_word) and bisect_search_itr(word_list, s_word):
                file.write(f'{word} : {f_word}, {s_word}\n')

def interlock_three(word_list):
    file = open("interlock_threes.txt", 'w+')
    for word in word_list:
        if len(word) > 2:
            f_word = word[::3]
            s_word = word[1::3]
            t_word = word[2::3]
            if bisect_search_itr(word_list, f_word) \
                and bisect_search_itr(word_list, s_word) \
                and bisect_search_itr(word_list, t_word):
                file.write(f'{word} : {f_word}, {s_word}, {t_word}\n')

word_list = build_word_list()
words_len = len(word_list)
interlock_three(word_list)
interlock_two(word_list)


# runtime_itr()
# runtime_recursive()