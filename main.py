def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    print("Hello world")
    print("Word Count: " + str(get_word_count(text)))

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def get_word_count(string):
    return len(string.split())

main()