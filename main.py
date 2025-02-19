def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(num_chars)


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

main()