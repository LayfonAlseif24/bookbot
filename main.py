def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_chars_count(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    chars_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["num"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
main()
