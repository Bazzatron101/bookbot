import sys
from stats import get_num_words
from stats import get_num_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents



def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    
    print("============ BOOKBOT ============")
    print(f"analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")

    print("--------- Character Count -------")

    num_chars = get_num_characters(book)

    for letter in num_chars:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")

    return 0



main()