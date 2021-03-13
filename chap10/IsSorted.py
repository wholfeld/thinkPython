# def is_sorted(t):
#     for idx in range(len(t)-1):
#         if t[idx] > t[idx + 1]:
#             return False
#     return True

def is_sorted(t):
    return t == sorted(t)


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
