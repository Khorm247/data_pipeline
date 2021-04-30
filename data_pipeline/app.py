import pipeline as pl


FILE_NAME = 'techcrunch.csv'


def main():
    result = pl.load_data(FILE_NAME)
    print(result)
    for dict_ in result:
        print("=> ", dict_)


if __name__ == '__main__':
    main()