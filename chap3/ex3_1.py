def right_justify(string):
    space = ' ' * (70 - len(string))
    print(space + string)


right_justify('monty')
right_justify('my longer string')
