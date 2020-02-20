from typing import List


class Book:
    def __init__(self, book_id: int, score: int):
        self.id = book_id
        self.score = score

    def __str__(self):
        return f"book id: {self.id} book_score: {self.score}"

    def __hash__(self):
        return self.id

    def __eq__(self, value):
        return self.id == value.id

    @classmethod
    def parse_from_line(cls, line: str):
        return [cls(book_id, int(book_score)) for book_id, book_score in enumerate(line.split())]
    
class Library:
    def __init__(self, library_id: int, registration_time: int, throughput: int):
        self.id = library_id
        self.books: List[Book] = []
        self.registration_time = registration_time
        self.throughput = throughput

    @property
    def number_of_books(self):
        return len(self.books)

    def add_books(self, books: List[Book]):
        self.books = books

    def __str__(self):
        books_string = list(map(str, self.books))
        return f"books: {books_string} registration_time:{self.registration_time} throughput:{self.throughput}"

    @classmethod
    def parse_from_lines(cls, library_id: int, library_definition: str):
        _, registration_time, throughput = map(int, library_definition.split())
        return cls(library_id, registration_time, throughput)

class RoundConfig:
    def __init__(self, books_number: int, libraries_number: int, days_number: int):
        self.books_number = books_number
        self.libraries_number = libraries_number
        self.days_number = days_number
        self.libraries: List[Library] = []
        self.books: List[Book] = []

    def __str__(self):
        books_string = list(map(str, self.books))
        library_string = list(map(str, self.libraries))
        return f"books number: {self.books_number} libraries number: {self.libraries_number} days: {self.days_number}\nbooks: {books_string}\nlibraries_string: {library_string}"

    @classmethod
    def parse_from_line(cls, line: str):
        """
        Create he RoundConfig from a data line.
        """
        books_number, libraries_number, days_number = map(int, line.split())
        return cls(books_number, libraries_number, days_number)