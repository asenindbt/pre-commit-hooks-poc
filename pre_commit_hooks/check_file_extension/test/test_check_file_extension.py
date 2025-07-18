from __future__ import annotations

from unittest import TestCase
from unittest.mock import MagicMock

from pre_commit_hooks.check_file_extension.main import (
    CheckFileExtensions,
)
from pre_commit_hooks.check_file_extension.main import (
    DataFileDetectedException,
)
from pre_commit_hooks.check_file_extension.main import (
    DataFileDetectedWarning,
)
from pre_commit_hooks.check_file_extension.main import (
    InvalidLogLevelException,
)


class Arguments:

    def __init__(self):
        self.filenames = None
        self.log_level = None


class TestCheckFileExtensions(TestCase):

    def setUp(self):
        self.mock_argparse = MagicMock()

    def test_no_data_files_log_level_type_error(self):

        # Arrange
        filenames_in_commit = ['a.txt', 'b.txt', 'c.txt']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'ERROR'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act
        actual = CheckFileExtensions(
            parser=self.mock_argparse,
        ).check_commit_file_extensions()

        # Assert
        self.assertEqual(actual, filenames_in_commit)

    def test_data_files_detected_log_level_type_error(self):

        # Arrange
        filenames_in_commit = ['a.csv', 'b.parquet', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'ERROR'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_some_data_files_detected_log_level_type_error(self):

        # Arrange
        filenames_in_commit = ['a.py', 'b.sh', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'ERROR'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_no_data_files_log_level_type_warning(self):

        # Arrange
        filenames_in_commit = ['a.txt', 'b.txt', 'c.txt']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'WARNING'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act
        actual = CheckFileExtensions(
            parser=self.mock_argparse,
        ).check_commit_file_extensions()

        # Assert
        self.assertEqual(actual, filenames_in_commit)

    def test_data_files_detected_log_level_type_warning(self):

        # Arrange
        filenames_in_commit = ['a.csv', 'b.parquet', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'WARNING'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertWarns(DataFileDetectedWarning):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_some_data_files_detected_log_level_type_warning(self):

        # Arrange
        filenames_in_commit = ['a.py', 'b.sh', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'WARNING'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertWarns(DataFileDetectedWarning):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_no_data_files_log_level_type_not_defined(self):

        # Arrange
        filenames_in_commit = ['a.txt', 'b.txt', 'c.txt']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act
        actual = CheckFileExtensions(
            parser=self.mock_argparse,
        ).check_commit_file_extensions()

        # Assert
        self.assertEqual(actual, filenames_in_commit)

    def test_data_files_detected_log_level_type_not_defined(self):

        # Arrange
        filenames_in_commit = ['a.csv', 'b.parquet', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_some_data_files_detected_log_level_type_not_defined(self):

        # Arrange
        filenames_in_commit = ['a.py', 'b.sh', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_no_data_files_log_level_type_invalid(self):

        # Arrange
        filenames_in_commit = ['a.txt', 'b.txt', 'c.txt']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'INVALID_LOG_LEVEL'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(InvalidLogLevelException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_data_files_detected_log_level_type_invalid(self):

        # Arrange
        filenames_in_commit = ['a.csv', 'b.parquet', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'INVALID_LOG_LEVEL'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(InvalidLogLevelException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_some_data_files_detected_log_level_type_invalid(self):

        # Arrange
        filenames_in_commit = ['a.py', 'b.sh', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'INVALID_LOG_LEVEL'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(InvalidLogLevelException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_data_files_detected_log_level_type_error_lower_case(self):

        # Arrange
        filenames_in_commit = ['a.py', 'b.sh', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'error'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertRaises(DataFileDetectedException):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()

    def test_data_files_detected_log_level_type_warning_lower_case(self):

        # Arrange
        filenames_in_commit = ['a.py', 'b.sh', 'c.json']

        arguments = Arguments()
        arguments.filenames = filenames_in_commit
        arguments.log_level = 'warning'

        self.mock_argparse.ArgumentParser().parse_args = (
            MagicMock(return_value=arguments)
        )

        # Act and Assert
        with self.assertWarns(DataFileDetectedWarning):
            CheckFileExtensions(
                parser=self.mock_argparse,
            ).check_commit_file_extensions()
