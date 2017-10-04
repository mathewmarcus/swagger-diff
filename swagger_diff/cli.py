from argparse import ArgumentParser, FileType

parser = ArgumentParser(description="Test the backwards compatbility of API changes by comparing Swagger docs")
parser.add_argument('old_swagger', type=FileType('r'))
parser.add_argument('new_swagger', type=FileType('r'))

args = parser.parse_args()


def main():
    pass

if __name__ == '__main__':
    main()
