from stats import get_word_count, get_character_count, report
import sys

def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_count = get_character_count(file_contents)
        return report(word_count, char_count)


def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    get_book_text(book_path)

main()