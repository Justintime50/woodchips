import inspect
import logging
import os
import tempfile
from unittest.mock import (
    mock_open,
    patch,
)

import pytest

import woodchips


MOCK_LOG_PATH = os.path.join("test", "mock-dir")
LOG_PATH_EXISTS = os.path.join("test", "logs")
LOG_LEVEL = "INFO"


@patch("os.makedirs")
def test_logger_class(mock_make_dirs):
    """Test setting up the Woodchips `Logger` class works correctly."""
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(
        name=function_name,
    )

    assert my_logger._logger.name == function_name
    assert logging.getLevelName(my_logger._logger.getEffectiveLevel()) == "INFO"


def test_log_to_console():
    """Test that the console handler gets setup correctly."""
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(name=function_name)
    my_logger.log_to_console()

    assert isinstance(my_logger._logger.handlers[0], logging.StreamHandler)
    assert my_logger._logger.handlers[0].formatter._fmt == "%(message)s"


def test_log_to_console_with_formatter():
    """Test that the console handler gets setup correctly with a formatter."""
    function_name = inspect.stack()[0][3]

    my_logger = woodchips.Logger(name=function_name)
    my_logger.log_to_console(formatter="%(asctime)s")

    assert isinstance(my_logger._logger.handlers[0], logging.StreamHandler)
    assert my_logger._logger.handlers[0].formatter._fmt == "%(asctime)s"


@pytest.mark.parametrize(
    "log_level, expected_log_value",
    [
        ("CRITICAL", 50),
        ("ERROR", 40),
        ("WARNING", 30),
        ("INFO", 20),
        ("DEBUG", 10),
        ("notset", 0),  # lowercased to ensure we uppercase all user input for this var
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

    with pytest.raises(KeyError) as error:
        my_logger = woodchips.Logger(name=function_name, level="BAD_LOG_LEVEL")
        my_logger._validate_log_level()

    assert (
        str(error.value) == "\"Could not setup Woodchips due to invalid log level: 'BAD_LOG_LEVEL', must be one of"
        " dict_keys(['CRITICAL',"
        " 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'])\""
    )


def test_log_to_file():
    """Tests that the file handler gets setup correctly."""
    function_name = inspect.stack()[0][3]

    with tempfile.TemporaryDirectory() as temp_dir:
        my_logger = woodchips.Logger(name=function_name)
        my_logger.log_to_file(
            location=temp_dir,
            formatter="%(asctime)s",
            log_size=10000,
            num_of_logs=2,
        )

        assert isinstance(my_logger._logger.handlers[0], logging.handlers.RotatingFileHandler)
        assert my_logger._logger.handlers[0].formatter._fmt == "%(asctime)s"
        assert function_name in my_logger._logger.handlers[0].baseFilename
        assert my_logger._logger.handlers[0].maxBytes == 10000
        assert my_logger._logger.handlers[0].backupCount == 2
        assert os.path.exists(temp_dir)


@patch("os.makedirs")
def test_log_to_file_dir_doesnt_exist(mock_makedirs):
    """Tests that the file handler gets setup correctly when no `location` exists already."""
    function_name = inspect.stack()[0][3]

    with patch("builtins.open", mock_open()):
        my_logger = woodchips.Logger(name=function_name)
        my_logger.log_to_file(location="mock_dir")

    mock_makedirs.assert_called_once()


def test_get_logger():
    """Tests that we `get` a logger instance by name."""
    custom_logger_name = "custom_logger_name"

    my_logger = woodchips.Logger(
        name=custom_logger_name,
    )

    retrieved_logger = woodchips.get(custom_logger_name)

    assert retrieved_logger == my_logger._logger
    assert retrieved_logger.name == my_logger.name == custom_logger_name
