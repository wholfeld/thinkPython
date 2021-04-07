from os.path import dirname, join
from random import choice

class Markov:
    def __init__(self, books, prefix_len: int=2, suffix_len: int=2):
        self.books = books
        self.markov_dict = dict()
        self.prefix = None
        self.prefix_len = prefix_len
        self.suffix_len = suffix_len

    def create_markov_dict(self, ):
        words_array = self.get_book_words_list()
        markov_dict = self.markov_dict
        for i in range(len(words_array)):
            prefix_end = self.prefix_len + i
            suffix_end = prefix_end + self.suffix_len
            if suffix_end < len(words_array):
                prefix_tuple = (" ".join(words_array[i:prefix_end]))
                markov_dict.setdefault(prefix_tuple, []).append(words_array[prefix_end:suffix_end])
        return markov_dict

    def get_book_words_list(self, book:str="")-> list:
        if not book:
            book = self.books[0]
        words_array = []
        current_dir = dirname(__file__)
        book = join(current_dir, "./" + book)

        with open(book, "r", encoding='utf8') as book:
            while True:
                line = book.readline()
                words_split = line.split()
                for i in range(len(words_split)):
                    words_split[i] = words_split[i].strip()

                if not line:
                    break
                words_array.extend(words_split)
        return words_array
    
    def create_text(self, length:int=80):
        self.prefix = self.get_seed()
        text = []
        for i in range(length):
            text.append(self.prefix.split()[0])
            self.get_next_suffix()
        print(" ".join(text))

    def get_seed(self)->str:
        seed = choice(list(self.markov_dict.keys()))
        return seed

    def get_next_suffix(self)->str:
        next_suffix = choice(self.markov_dict[self.prefix])
        prefix = self.prefix
        self.prefix = " ".join(prefix.split()[1:] + next_suffix[:-1])


books = ["franken_clean2.txt"]
markov = Markov(books, prefix_len=2)
markov.get_book_words_list()
markov.create_markov_dict()
markov.create_text()
# markov.create_text(20)

