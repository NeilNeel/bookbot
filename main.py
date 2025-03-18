
def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as f:
        file_contents = f.read()
        return get_word_count(file_contents)

def get_word_count(text_content):
    words = text_content.split()
    count = len(words)
    return (f"{count} words found in the document")

def main():
    print(get_book_text("./books/frankenstein.txt"))


main()