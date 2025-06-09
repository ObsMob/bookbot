def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count

def main():
    filepath = "books/frankenstein.txt"
    num_words = word_count(get_book_text(filepath))
    print(f"{num_words} words found in the document")

main()