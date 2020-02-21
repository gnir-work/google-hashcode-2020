from parser import parse_file
from typing import List, Dict
from models import *

def main():
    round_config = parse_file('b_read_on.txt')
    libraries = iter(sorted(round_config.libraries, key=lambda lib: lib.registration_time))
    remaining_days = round_config.days_number
    books_number_from_each_library = {}
    libraries_to_scan = []
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