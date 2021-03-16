import timeit


def bisect_search_itr(word_list, search_word):
    left_idx = 0
    right_idx = len(word_list)
    while left_idx <= right_idx:
        # left = 1 and right = 1 round to 0 if using // 2 so need to use float and cast to int
        mid = int(left_idx / 2 + right_idx / 2)
        if search_word > word_list[mid]:
            left_idx = mid + 1
        elif search_word < word_list[mid]:
            right_idx = mid - 1
        else:
            return True
    return False


def run_dict_speed():
    word_dict = dict()
    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_dict[line.strip()] = None

    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            if line.strip() not in word_dict:
                print("dict wtf")


def run_list_speed():
    word_list = []
    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_list.append(line.strip())

    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            if not bisect_search_itr(word_list, line.strip()):
                print("list wtf")


def runtime(func_name, f):
    start = timeit.default_timer()
    f()
    stop = timeit.default_timer()
    print(f'The runtime of {func_name} was {stop-start}')


runtime('diction speed function', run_dict_speed)
runtime('list speed function', run_list_speed)
