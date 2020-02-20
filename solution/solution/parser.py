FILE_NAME = "data.txt"
from models import RoundConfig, Book, Library

def get_file_lines(path_to_file: str):
    with open(path_to_file) as data_file:
        for line in data_file.readlines():
            yield line

def parse_file(path_to_file: str):
    data_lines = get_file_lines(path_to_file)
    round_config: RoundConfig = RoundConfig.parse_from_line(next(data_lines))
    books = Book.parse_from_line(next(data_lines))
    round_config.books = books
    for library_id in range(round_config.libraries_number):
        library_data = next(data_lines)
        library_books = next(data_lines)
        library = Library.parse_from_lines(library_id, library_data)
        library_books_ids = map(int, library_books.split())
        library.add_books([round_config.books[book_id] for book_id in library_books_ids])
        round_config.libraries.append(library)
         
    return round_config

if __name__ == "__main__":
    print(parse_file(FILE_NAME))