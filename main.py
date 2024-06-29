def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"The word count is {word_count}.")
    message = dec_message(char_count)
    for i in message:
        print(f"The character '{i['name']}' appears {i['count']} times.")
    print(f"--- End report of {book_path} ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["count"]

def dec_message(dict):
    chars = []
    for key in dict:
        chars.append({
            "name": key,
            "count": dict[key]
        })
    chars.sort(reverse=True,key=sort_on)
    return chars


def count_characters(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if not char.isalpha():
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()