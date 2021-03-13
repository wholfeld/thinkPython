import timeit

file_out = open("words_out.txt", 'w+')


def efficient_list():
    word_list = []
    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_list.append(line.strip())


def inefficient_list():
    word_list = []
    with open("words.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            word_list = word_list + [line.strip()]


def runtime(func_name, f):
    start = timeit.default_timer()
    f()
    stop = timeit.default_timer()
    print(f'your function {func_name} took {stop - start} to run.\n')


runtime("efficient list", efficient_list)
runtime("inefficient list", inefficient_list)

# inefficient_list()
