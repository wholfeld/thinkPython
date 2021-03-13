def nested_sum(t):
    sum = 0
    for item in t:
        if type(item) == list:
            sum += nested_sum(item)
        else:
            sum += item
    return sum

t = [[[1, 2]], [3], [4, 5, 6]]
print(nested_sum(t))
