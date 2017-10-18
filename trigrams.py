"""Trigram Algorithim to write a story based on a story."""
import random


def fill_book_dict(path):
    """Fill out book_dict."""
    book = open(path).read().replace('\n', " ").split(" ")
    book_iterator = iter(book)
    next(book_iterator)
    book_output = [" ".join((first_word, second_word))
                   for first_word, second_word
                   in zip(book, book_iterator)]
    book_dict = {}
    for word in range(len(book_output)):
        try:
            key_group = book_dict.setdefault(book_output[word], [])
            key_group.append(book[word + 2])
        except IndexError:
            key_group = book_dict.setdefault(book_output[word], [])
    return book_dict


def make_first_key(path, book_dict):
    """Find a random key."""
    first_key = random.choice(list(book_dict))
    return first_key


def main(text, number):
    """Currently does nothing."""
    book_dict = fill_book_dict(text)
    search_key = make_first_key(text, book_dict)
    generated_text = ""
    for x in range(number):
        new_text = book_dict[search_key][random.randint(0,
                                         len(book_dict[search_key]) - 1)]
        generated_text += "%s " % new_text
        search_key = search_key.split(' ')[1] + " " + new_text
    return generated_text
