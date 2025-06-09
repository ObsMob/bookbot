import sys
    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import character_dict
from stats import dict_sort

def main(): 
    num_words = word_count(get_book_text(filepath))
    character_count = character_dict(get_book_text(filepath))
    sorted = dict_sort(character_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["value"]}")
    print("============= END ===============")
main()