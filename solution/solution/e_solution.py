from parser import parse_file
from typing import List, Dict
from models import *

def get_score(lib, sum_of_books):
    books_score = sum([book.score for book in lib.books]) / sum_of_books * 100
    score = (lib.throughput ** 2 / (lib.registration_time))
    print(books_score, score) 
    return score + books_score 

def main():
    round_config, _ = parse_file('f_libraries_of_the_world.txt')
    sum_of_books = sum([book.score for book in round_config.books])
    libraries = iter(sorted(round_config.libraries, key=lambda lib: get_score(lib, sum_of_books), reverse=True))
    remaining_days = round_config.days_number
    books_number_from_each_library = {}
    libraries_to_scan = []
    print(sum_of_books)
    while remaining_days > 0:
        library = next(libraries)
        remaining_days -= library.registration_time
        books_number_from_each_library[library.id] = library.number_of_books
        libraries_to_scan.append(library)
    
    __generate_output(libraries_to_scan, books_number_from_each_library)


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