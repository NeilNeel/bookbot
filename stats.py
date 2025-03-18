
def get_word_count(text_content):
    words = text_content.split()
    count = len(words)
    return count

def get_character_count(text_content):
    char_count = {}
    for word in text_content:
        for char in word.lower().split():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

# def sort_on(dict):
#     return dict

def report(word_count, char_count):
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    report_output = "============ BOOKBOT ============\n"
    report_output += "Analyzing book found at books/frankenstein.txt...\n"
    report_output += "----------- Word Count ----------\n"
    report_output += f"Found {word_count} total words\n"
    report_output += "--------- Character Count -------\n"

    for key in sorted_char_count:
        report_output += f"{key}: {char_count[key]}\n"

    report_output += "============= END ==============="
    return print(report_output)