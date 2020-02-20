FILE_NAME = "data.txt"
from .models import RoundConfig, Book, Library

def get_file_lines(path_to_file: str):
    with open(path_to_file) as data_file:
        for line in data_file.readlines():
            yield line

def parse_file(path_to_file: str):
    data_lines = get_file_lines(path_to_file)
    round_config = RoundConfig.parse_from_line(next(data_lines))


    return round_config

if __name__ == "__main__":
    print(parse_file(FILE_NAME))