
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
