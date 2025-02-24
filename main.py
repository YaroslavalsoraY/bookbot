from stats import get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Report of book: {book_path[:-4]} ---")
    print(f"{num_words} words found in the document")
    print_num_chars(get_num_chars(text))
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_chars(text):
    chars_dict = {}
    for char in text.lower():
        if char.lower() in chars_dict:
            continue
        else:
            chars_dict[char.lower()] = text.lower().count(char)
    return chars_dict


def sort_on(items):
    return items[1]


def print_num_chars(num_chars):
    num_chars_list = list(num_chars.items())
    num_chars_list_s = sorted(num_chars_list, key=sort_on, reverse=True)
    for el in sorted(num_chars_list, key=sort_on, reverse=True):
        if el[0].isalpha():   
            print(f"{el[0]}: {el[1]}")
        else:
            continue

main()