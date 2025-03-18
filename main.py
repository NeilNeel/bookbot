from stats import get_word_count, get_character_count, report

def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_count = get_character_count(file_contents)
        return report(word_count, char_count)


def main():
    get_book_text("./books/frankenstein.txt")

main()