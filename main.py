
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    print(text)

def get_book_text(path):
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents
