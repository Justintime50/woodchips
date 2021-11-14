import logging
import logging.handlers
import os

# 200kb * 5 files = 1mb of logs
# TODO: Allow these to be configurable by the user
DEFAULT_LOG_MAX_BYTES = 200000  # 200kb
DEFAULT_LOG_BACKUP_COUNT = 5


def setup(logger_name: str, log_location: str, log_level: str = 'INFO') -> logging.Logger:
    """Setup project logging based on configuration.

    Each module that requires logging should instantiate this function and pass a
    new name based on the module using logging, which for most purposes should be
    `__name__` passed as `logger_name`.

    TODO: Allow the user to specify if they want console/file logging or not.
    """
    # Create the logger
    logger_instance = logging.getLogger(logger_name)
    log_levels = {
        'CRITICAL': logging.CRITICAL,  # 50
        'ERROR': logging.ERROR,  # 40
        'WARNING': logging.WARNING,  # 30
        'INFO': logging.INFO,  # 20
        'DEBUG': logging.DEBUG,  # 10
        'NOTSET': logging.NOTSET,  # 0
    }

    try:
        selected_log_level = log_levels[log_level.upper()]
    except KeyError as error:
        raise KeyError(
            f'Could not setup Woodchips due to invalid log level: {error}, must be one of {log_levels.keys()}'  # noqa
        )

    logger_instance.setLevel(selected_log_level)

    # Setup console handling
    console_handler = logging.StreamHandler()
    logger_instance.addHandler(console_handler)

    # Setup file handling
    if not os.path.exists(log_location):
        os.makedirs(log_location)

    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    log_file = os.path.join(log_location, 'woodchips.log')
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=DEFAULT_LOG_MAX_BYTES,
        backupCount=DEFAULT_LOG_BACKUP_COUNT,
    )
    file_handler.setFormatter(file_formatter)
    logger_instance.addHandler(file_handler)

    return logger_instance
