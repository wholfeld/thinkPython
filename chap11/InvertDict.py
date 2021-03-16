def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        # if val not in inverse:
        #     inverse[val] = [key]
        # else:
        #     inverse[val].append(key)
        inverse.setdefault(val, []).append(key)
    return inverse


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d



hist = histogram('parrot')
inverse = invert_dict(hist)
print(inverse)