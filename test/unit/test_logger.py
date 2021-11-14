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
def test_setup(mock_make_dirs):
    """Test setting up logging works correctly while asserting the level, formatter,
    handlers, and path are all correct.
    """
    with patch('builtins.open', mock_open()):
        logger = woodchips.setup(
            logger_name=__name__,
            log_location=MOCK_LOG_PATH,
            log_level=LOG_LEVEL,
        )

    mock_make_dirs.assert_called_once()
    assert logging.getLevelName(logger.getEffectiveLevel()) == 'INFO'

    # The following get set from the file handler but are tested here since we have the
    # complete instance returned from this function.
    assert logger.handlers[1].formatter._fmt == '%(asctime)s - %(levelname)s - %(message)s'
    assert 'test/mock-dir/test.log' in logger.handlers[1].baseFilename
    assert woodchips.logger.DEFAULT_LOG_MAX_BYTES == logger.handlers[1].maxBytes
    assert woodchips.logger.DEFAULT_LOG_BACKUP_COUNT == logger.handlers[1].backupCount


def test_setup_console_handler():
    """Test that the console handler gets setup without breaking."""
    woodchips.logger._setup_console_handler(logging.getLogger(__name__))


@pytest.mark.parametrize(
    'log_level, expected_log_value',
    [
        ('CRITICAL', 50),
        ('ERROr', 40),
        ('WARNING', 30),
        ('INFO', 20),
        ('DEBUG', 10),
        ('NOTSET', 0),
    ],
)
def test_validate_log_level(log_level, expected_log_value):
    """Tests that we map log levels correctly."""
    active_log_level = woodchips.logger._validate_log_level(log_level)

    assert active_log_level == expected_log_value


def test_validate_log_level_invalid():
    """Test that we raise an error when a bad log level is passed in."""
    with patch('builtins.open', mock_open()):
        with pytest.raises(KeyError) as error:
            woodchips.logger._validate_log_level('BAD_LOG_LEVEL')

    assert (
        str(error.value)
        == '"Could not setup Woodchips due to invalid log level: \'BAD_LOG_LEVEL\', must be one of'
        ' dict_keys([\'CRITICAL\','
        ' \'ERROR\', \'WARNING\', \'INFO\', \'DEBUG\', \'NOTSET\'])"'
    )


def test_setup_file_handler_dir_does_not_exist():
    """Tests that we create the log path correctly.

    NOTE: Other tests related to this function are tested in the `setup` tests.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        woodchips.logger._setup_file_handler(
            logger_instance=logging.getLogger(__name__),
            log_location=temp_dir,
        )

        assert os.path.exists(temp_dir)
