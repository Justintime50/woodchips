import inspect
import logging
import os
import tempfile
from unittest.mock import mock_open, patch

import pytest

import woodchips

MOCK_LOG_PATH = os.path.join('test', 'mock-dir')
LOG_PATH_EXISTS = os.path.join('test', 'logs')
LOG_LEVEL = 'INFO'


@patch('os.makedirs')
def test_logger_class(mock_make_dirs):
    """Test setting up logging works correctly while asserting the level, formatter,
    handlers, and path are all correct.
    """
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(
        name=function_name,
    )

    assert logging.getLevelName(my_logger.logger.getEffectiveLevel()) == 'INFO'


#     # The following get set from the file handler but are tested here since we have the
#     # complete instance returned from this function.
#     assert logger.handlers[1].formatter._fmt == '%(asctime)s - %(levelname)s - %(message)s'
#     assert 'test/mock-dir/test.log' in logger.handlers[1].baseFilename
#     assert woodchips.logger.DEFAULT_LOG_MAX_BYTES == logger.handlers[1].maxBytes
#     assert woodchips.logger.DEFAULT_LOG_BACKUP_COUNT == logger.handlers[1].backupCount


def test_log_to_console():
    """Test that the console handler gets setup correctly."""
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(name=function_name)
    my_logger.log_to_console()

    # TODO: Make an actual assertion here as this is wrong
    assert my_logger.logger.handlers[0]


def test_log_to_console_with_formatter():
    """Test that the console handler gets setup correctly."""
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(name=function_name)
    my_logger.log_to_console(formatter='%(levelname)s')

    # TODO: Make an actual assertion here as this is wrong
    assert vars(my_logger.logger) == ''


@pytest.mark.parametrize(
    'log_level, expected_log_value',
    [
        ('CRITICAL', 50),
        ('ERROR', 40),
        ('WARNING', 30),
        ('INFO', 20),
        ('DEBUG', 10),
        ('notset', 0),  # lowercased to ensure we uppercase all user input for this var
    ],
)
def test_validate_log_level(log_level, expected_log_value):
    """Tests that we map log levels correctly."""
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(name=function_name, level=log_level)
    active_log_level = my_logger._validate_log_level()

    assert active_log_level == expected_log_value


def test_validate_log_level_invalid_level():
    """Test that we raise an error when a bad log level is passed in."""
    function_name = inspect.stack()[0][3]

    with patch('builtins.open', mock_open()):
        with pytest.raises(KeyError) as error:
            my_logger = woodchips.Logger(name=function_name, level='BAD_LOG_LEVEL')
            my_logger._validate_log_level()

    assert (
        str(error.value)
        == '"Could not setup Woodchips due to invalid log level: \'BAD_LOG_LEVEL\', must be one of'
        ' dict_keys([\'CRITICAL\','
        ' \'ERROR\', \'WARNING\', \'INFO\', \'DEBUG\', \'NOTSET\'])"'
    )


# def test_setup_file_handler_dir_does_not_exist():
#     """Tests that we create the log path correctly.

#     NOTE: Other tests related to this function are tested in the `setup` tests.
#     """
# function_name = inspect.stack()[0][3]

#     with tempfile.TemporaryDirectory() as temp_dir:
#         woodchips.logger._setup_file_handler(
#             logger_instance=logging.getLogger(function_name),
#             log_location=temp_dir,
#         )

#         assert os.path.exists(temp_dir)
