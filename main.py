
def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()