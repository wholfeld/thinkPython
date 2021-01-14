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


def print_string(string):
    print(string, end=' ')


def do_one_do_four(f, arg, arg2):
    f(arg)
    do_four(f, arg2)

def draw_box


do_one_do_four(print_string, '+', ' -')
do_one_do_four(print_string, '+', ' -')
#do_one_do_four(print_string('|'), print_string('  '))
# line_segment('|', '  ')
