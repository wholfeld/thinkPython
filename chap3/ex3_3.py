def do_twice(f, arg):
    f(arg)
    f(arg)


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


def print_twice(string):
    print(string)
    print(string)


def line_segment(char_start, str_rep):
    print_string(char_start)
    do_four(print_string, str_rep)
    print()


def do_nothing(arg):
    return


def print_string(string):
    print(string, end=' ')


def one_four_one(f, arg, f2, arg2, f3, arg3):
    f(arg)
    do_four(f2, arg2)
    f3(arg3)


def draw_columns(columns):
    for j in range(5):
        for k in range(columns - 1):
            one_four_one(print_string, '|', print_string, '  ', do_nothing, '')
        one_four_one(print_string, '|', print_string, '  ', print_string, '|')
        print()


def draw_boxes(columns, rows):
    for i in range(rows):
        for j in range(columns - 1):
            one_four_one(print_string, '+', print_string, ' -', do_nothing, '')
        one_four_one(print_string, '+', print_string, ' -', print_string, '+')
        print()

        draw_columns(columns)

    for j in range(columns - 1):
        one_four_one(print_string, '+', print_string, ' -', do_nothing, '')
    one_four_one(print_string, '+', print_string, ' -', print_string, '+')
    print()


# do_one_do_four(print_string, '+', ' -')
# do_one_do_four(print_string, '+', ' -')
draw_boxes(3, 2)
#do_one_do_four(print_string('|'), print_string('  '))
# line_segment('|', '  ')
