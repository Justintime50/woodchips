import logging
import os
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
    assert logger.handlers[1].formatter._fmt == '%(asctime)s - %(levelname)s - %(message)s'
    assert 'test/mock-dir/test.log' in logger.handlers[1].baseFilename
    assert woodchips.logger.DEFAULT_LOG_MAX_BYTES == logger.handlers[1].maxBytes
    assert woodchips.logger.DEFAULT_LOG_BACKUP_COUNT == logger.handlers[1].backupCount


@patch('os.makedirs')
def test_setup_bad_log_level(mock_make_dirs):
    """Test that we raise an error when a bad log level is passed in."""
    with patch('builtins.open', mock_open()):
        with pytest.raises(KeyError) as error:
            _ = woodchips.setup(
                logger_name=__name__,
                log_location=MOCK_LOG_PATH,
                log_level='BAD_LOG_LEVEL',
            )

    assert (
        str(error.value)
        == '"Could not setup Woodchips due to invalid log level: \'BAD_LOG_LEVEL\', must be one of'
        ' dict_keys([\'CRITICAL\','
        ' \'ERROR\', \'WARNING\', \'INFO\', \'DEBUG\', \'NOTSET\'])"'
    )


@patch('os.makedirs')
@patch('woodchips.logger')
def test_setup_logging_dir_exists(mock_logger, mock_make_dirs):
    # TODO: Mock this better so we don't need a gitignored empty folder for testing
    if not os.path.exists(LOG_PATH_EXISTS):
        os.mkdir(LOG_PATH_EXISTS)

    _ = woodchips.setup(
        logger_name=__name__,
        log_location=LOG_PATH_EXISTS,
        log_level=LOG_LEVEL,
    )
