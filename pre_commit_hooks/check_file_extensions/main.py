# print_arguments/main.py
import argparse


class DataFileDetectedException(Exception):
    def __init__(self):
        self.message = "Files containing data is detected. Data files are not allowed to be pushed into GitHub."
        super().__init__(self.message)


class CheckFileExtensions:
    def __init__(self, argparse):
        self.argparse = argparse
        self.invalid_extensions = \
            (".csv", ".tsv", ".xlsx", ".xls", ".parquet", ".json", ".xml", ".png", ".pdf", ".rdata", ".rds")

    def check_commit_file_extensions(self):
        parser = self.argparse.ArgumentParser()
        parser.add_argument("filenames", nargs="*")
        args = parser.parse_args()

        self.print_arguments(args.filenames)

        return args.filenames

    def print_arguments(self, arguments: list[str]):
        for argument in arguments:
            if argument.endswith(self.invalid_extensions):
                raise DataFileDetectedException()


def main():
    filenames = CheckFileExtensions(argparse=argparse).check_commit_file_extensions()
    print(filenames)


if __name__ == "__main__":
    main()