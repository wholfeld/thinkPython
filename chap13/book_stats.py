import re
import random


class books_stats():

    def __init__(self, title: str):
        self.book = title
        self.book_dict = {}
        self._build_book_dict()

    def print_top_word(self, count: int, common_words: set):
        words_tup = []
        for word in self.book_dict:
            if word not in common_words:
                words_tup.append((self.book_dict[word], word))
        words_tup.sort(key= lambda x: x[0], reverse=True)
        return 1

    def print_unique_words(self, words_set: set):
        unique_words = []
        for word in self.book_dict:
            if word not in words_set:
                unique_words.append(word)
        return unique_words

    def _build_book_dict(self):
        with open(self.book, "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break

                add_words(line.strip(), self.book_dict)
        return 1


def add_words(line: str, words_dict: dict):
    # remove puncuation
    res = re.sub(r'[^\w\s]', '', line)
    single_words = res.split(' ')
    for word in single_words:
        word = word.lower()
        words_dict[word] = words_dict.setdefault(word, 0) + 1


def get_word_set() -> set:
    words_set = set()
    with open("words.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            words_set.add(line.strip().lower())
    return words_set

def get_common_words(count: int)->set:
    common_words_set = set()
    with open("common_words.txt", "r") as file:
        while True:
            word = file.readline()
            if not word:
                break
            word = word.strip()
            common_words_set.add(word)
    return common_words_set


def clean_book(book_name: str):
    new_name = book_name[:-4] + "_clean.txt"
    start_reading = False
    with open(book_name, "r") as read_file:
        with open(new_name, "w+") as write_file:
            while True:
                line = read_file.readline()
                if not line:
                    break
                if start_reading:
                    if "*** END" in line:
                        break
                    else:
                        write_file.write(line)
                if "*** S" in line:
                    start_reading = True

def choose_from_hist(words_dict)-> str:
    count = 0
    words = []
    counts = []
    for word in words_dict:
        words.append(word)
        count += words_dict[word]
        counts.append(count)
    rand = random.randint(0, count)
    index = get_index(rand, counts, 0, len(counts)-1)
    return words[index]


def get_index(rand, counts, start, end):
    mid = (start + end) // 2
    if mid > (len(counts) - 1) or mid == 0:
        return mid
    if rand > counts[mid - 1]:
        if rand < counts[mid]:
            return mid
        else:
            return get_index(rand, counts, mid, end)
    else:
        return get_index(rand, counts, start, mid)

books_array = ["franken_clean.txt"]
# clean_book(books_array[])
words_set = get_word_set()
common_words = get_common_words(500)
book = books_stats(books_array[0])
book.print_unique_words(words_set)
book.print_top_word(20, common_words)
print(choose_from_hist(book.book_dict))
