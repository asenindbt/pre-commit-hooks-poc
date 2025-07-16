from unittest import TestCase
from unittest.mock import MagicMock
from pre_commit_hooks.check_file_extensions.main import CheckFileExtensions
from pre_commit_hooks.check_file_extensions.main import DataFileDetectedException


class Arguments:

    def __init__(self):
        self.filenames = None


class TestCheckFileExtensions(TestCase):

    def setUp(self):
        self.mock_argparse = MagicMock()

    def test_check_commit_file_extensions_all_files_valid(self):

        # Arrange
        filenames_in_commit = ["a.txt", "b.txt", "c.txt"]

        arguments = Arguments()
        arguments.filenames = filenames_in_commit

        self.mock_argparse.ArgumentParser().parse_args = MagicMock(return_value=arguments)

        # Act
        actual = CheckFileExtensions(argparse=self.mock_argparse).check_commit_file_extensions()

        # Assert
        self.assertEqual(actual, filenames_in_commit)

    def test_check_commit_file_extensions_all_files_invalid(self):

        # Arrange
        filenames_in_commit = ["a.csv", "b.parquet", "c.json"]

        arguments = Arguments()
        arguments.filenames = filenames_in_commit

        self.mock_argparse.ArgumentParser().parse_args = MagicMock(return_value=arguments)

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(argparse=self.mock_argparse).check_commit_file_extensions()

    def test_check_commit_file_extensions_some_files_invalid(self):

        # Arrange
        filenames_in_commit = ["a.py", "b.sh", "c.json"]

        arguments = Arguments()
        arguments.filenames = filenames_in_commit

        self.mock_argparse.ArgumentParser().parse_args = MagicMock(return_value=arguments)

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(argparse=self.mock_argparse).check_commit_file_extensions()
