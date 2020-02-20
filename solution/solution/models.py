from typing import List

class Book:
    def __init__(self, book_id: int, score: int):
        self.id = book_id
        self.score = score
        self.library_ids: List[int] = []

    def add_library(self, library_id: int):
        """
        Add library to book
        """
        self.library_ids.append(library_id)
    
class Library:
    def __init__(self, library_id: int, books: List[Book], registration_time: int, throughput: int):
        self.id = library_id
        self.books = books
        self.registration_time = registration_time
        self.throughput = throughput


class RoundConfig:
    def __init__(self, books_number: int, libraries_number: int, days_number: int):
        self.books_number = books_number
        self.libraries_number = libraries_number
        self.days_number = days_number
        self.libraries: List[Library] = []
        self.books: List[Book] = []

    def __str__(self):
        return f"books number: {self.books_number} libraries number: {self.libraries_number} days: {self.days_number}"

    @classmethod
    def parse_from_line(cls, line: str):
        """
        Create he RoundConfig from a data line.
        """
        books_number, libraries_number, days_number = map(int, line.split())
        return cls(books_number, libraries_number, days_number)