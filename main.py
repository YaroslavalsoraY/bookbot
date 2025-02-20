def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Report of book: {book_path[:-4]} ---")
    print(f"{num_words} words found in the document")
    print_num_chars(get_num_chars(text))
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


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
            print(f"The '{el[0]}' character was found {el[1]} times")
        else:
            continue

main()