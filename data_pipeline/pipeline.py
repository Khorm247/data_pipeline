from pathlib import Path
from typing import Generator

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


# ETL Datapipeline: Extract, Transform, Load
def read_data_from_csv(file_name: str) -> Generator:
    """ große Datei einlesen """
    with open(DATA_DIR / file_name) as f:
        # content = f.read()
        for line in f:
            # print(line)
            yield line


def split_line(g: Generator) -> Generator:
    result = (line.strip().split(',') for line in g)
    return result


def dictify(g: Generator) -> Generator:
    header = next(g)
    # print("Dict: ", g)
    return (dict(zip(header, line)) for line in g)


def load_data(file_name: str) -> Generator:
    file_generator = read_data_from_csv(file_name)
    split_lines = split_line(file_generator)
    result = dictify(split_lines)
    return result


if __name__ == '__main__':
    load_data('techcrunch.csv')
    # print("Path: ", Path(__file__).resolve().parent.parent)
