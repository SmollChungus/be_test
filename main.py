def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    print(f"========Begin of count report on: {book_path}========")
    print(count_letters(text))
    print("========Counting complete========")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    text = text.lower()
    letter_counter = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1
    return letter_counter

main()