import anagram_sets as anagram_module
import dbm
import pickle
import shelve

# def db_anagrams_test():
#     d = {'opst': ['post', 'pots']}
#     d_dump = pickle.dumps(d)
#     db = dbm.open('anagram_db', 'c')
#     db['opst'] = d_dump

#     # pickle version
#     # print(db['opst'])

#     # unpickled version
#     # read_db = pickle.loads(db['opst'])
#     # print(read_db)

#     # shelve.Pickler()
#     # shelve.Shelf(d)

#     with shelve.open('spam') as shelve_db:
#         # shelve_db['eggs'] = 'egg'
#         for key in shelve_db.keys():
#             print(key)
#             print(shelve_db[key])
#         # shelve_db['d'] = d
    # db.close()
    # return
    # anagram_sets.print_anagram_sets(d)

def store_anagrams():
    all_anagrams = anagram_module.all_anagrams('words.txt')
    with shelve.open('anagrams_db', 'c') as shelve_db:
        shelve_db['all_anagrams'] = all_anagrams

def read_anagrams(word='test'):
    anagram_dict = None
    with shelve.open('anagrams_db')  as shelve_db:
        anagram_dict = shelve_db['all_anagrams']
    sig = anagram_module.signature(word)
    if sig in anagram_dict:
        print(anagram_dict[sig])

# store_anagrams()
read_anagrams('horse')
