from parser import parse_file
from typing import List, Dict
from models import *

def main():
    round_config, books_to_number_of_libraries = parse_file('d_tough_choices.txt')
    remaining_days = round_config.days_number
    books_number_from_each_library = {}
    libraries_to_scan = []

    print(books_to_number_of_libraries)
    # while remaining_days > 0:
    #     pass        
    # __generate_output(libraries_to_scan, books_number_from_each_library)


def build_book_to_number_of_libraries(books, libraries):
    book_to_number_of_libraries = {}
    for book in books:
        print(book)
        for library in libraries:
            if book in library.books:
                book_to_number_of_libraries[book] = book_to_number_of_libraries.get(book, 0) + 1
    return book_to_number_of_libraries


def __generate_output(scanned_libs: List[Library], num_books_from_libs: Dict[int, int]):
    with open("output.txt", "w+") as f:
        f.write(f"{len(scanned_libs)}\n")
        for i, lib in enumerate(scanned_libs):
            if i > 0:
                f.write("\n")
            f.write(f"{lib.id} {num_books_from_libs[lib.id]}\n")
            books_to_scan = sorted(lib.books, key=lambda b: b.score, reverse=True)[:num_books_from_libs[lib.id]]
            f.write(f"{' '.join([str(b.id) for b in books_to_scan])}")


if __name__ == '__main__':
    main()