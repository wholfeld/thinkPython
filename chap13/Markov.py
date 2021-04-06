
class Markov:
    def __init__(self, books):
        self.markov_dict = dict()
        self.books = books

def get_seed(markov_dict: dict)->str:
    return ""

def get_next_suffix(prefix, markov_dict)->str:
    return ""


books = ["franken.txt"]
markov = Markov(books)
markov.create_markov_dict(2, 2)
markov.create_text(20)

