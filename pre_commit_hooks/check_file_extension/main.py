# check_file_extension/main.py
from __future__ import annotations

import argparse
import warnings


class DataFileDetectedException(Exception):
    def __init__(self):
        self.message = (
            'Files containing data is detected. '
            'Data files are not allowed to be pushed into GitHub.'
        )
        super().__init__(self.message)


class InvalidLogLevelException(Exception):
    def __init__(self):
        self.message = (
            'Log level is invalid. Please specify a valid log level, '
            'either ERROR or WARNING.'
        )
        super().__init__(self.message)


class DataFileDetectedWarning(Warning):
    def __init__(self):
        self.message = (
            'Data files committed to GitHub detected. Please check '
            'if these files do not contain real data.'
        )
        super().__init__(self.message)


class CheckFileExtensions:
    def __init__(self, parser):
        self.parser = parser
        self.invalid_extensions = \
            (
                '.csv', '.tsv', '.xlsx', '.xls', '.parquet',
                '.json', '.xml', '.png', '.pdf', '.rdata', '.rds',
            )

    def check_commit_file_extensions(self) -> list[str]:
        parser = self.parser.ArgumentParser()
        # log_level = self.get_log_level(parser)
        commited_filenames = self.get_commited_filename_extensions(
            parser,
        )

        return commited_filenames

    # def get_log_level(self, parser):
    #     # TODO: This is causing an issue in getting the args from the command line
    #     parser.add_argument('--log-level', type=str)
    #     args = parser.parse_args()
    #
    #     if args.log_level is None:
    #         return None
    #     else:
    #         log_level = args.log_level.upper()
    #
    #         if log_level != 'ERROR' and log_level != 'WARNING':
    #             raise InvalidLogLevelException()
    #         else:
    #             return log_level

    def get_commited_filename_extensions(self, parser):
        parser.add_argument('--log-level', nargs='+', type=str)
        parser.add_argument('filenames', nargs='*', type=str)

        args = parser.parse_args()

        print(args.log_level)
        print(args.filenames)

        log_level = None

        if args.log_level is None:
            log_level = None
        else:
            log_level = args.log_level.upper()

            if log_level != 'ERROR' and log_level != 'WARNING':
                raise InvalidLogLevelException()

        for filename in args.filenames:
            if filename.endswith(self.invalid_extensions):

                if log_level == 'ERROR':
                    raise DataFileDetectedException()
                elif log_level == 'WARNING':
                    warnings.warn(DataFileDetectedWarning())
                else:
                    raise DataFileDetectedException()

        return args.filenames


def main():
    CheckFileExtensions(
        parser=argparse,
    ).check_commit_file_extensions()


if __name__ == '__main__':
    main()
