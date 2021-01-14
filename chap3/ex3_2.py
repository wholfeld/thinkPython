def do_twice(f, arg):
    f(arg)
    f(arg)


def print_twice(string):
    print(string)
    print(string)


def print_spam():
    print('spam')


def print_string(string):
    print(string)


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


# do_twice(print_twice, 'spam')
do_four(print_string, 'spam')
