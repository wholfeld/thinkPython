from collections import Counter, defaultdict

def has_no_e(word:str)->bool:
    return not any(c =='e' for c in word)


# print(has_no_e('fun'))
# print(has_no_e('read'))

def uses_all(word:str, required:str)->bool:
    # for c in required:
    #     if not any(c==s for s in word):
    #         return False
    # return True
    return all(letter in word for letter in required)

# print(uses_all('funny', 'fun'))
# print(uses_all('funny', 'sun'))

def avoids(word, forbidden):
    # return not any(letter in forbidden for letter in word)

    # dif = set(word) - set(forbidden)
    # return len(dif) == len(word)
    return len(set(word) - set(forbidden)) == len(word)

# print(avoids("laugh", "by"))
# print(avoids("laugh", "hi"))
count = Counter('parrot')
# print(count)

d = defaultdict(list)
t = d['new key']
# print(t)

l = list
# print(l)

def printall(*args, **kwargs):
    '''Prints all positional arguments and then all keyword arguments '''
    print(args, kwargs)

printall('fun', 3, third='3')