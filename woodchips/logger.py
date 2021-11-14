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
    new name based on the module using logging. Typically for most purposes, this
    should be `__name__` passed as `logger_name`.

    TODO: Allow the user to specify if they want console/file logging or not.
    """
    # Create the logger
    logger_instance = logging.getLogger(logger_name)
    active_log_level = _validate_log_level(log_level)
    logger_instance.setLevel(active_log_level)

    # Setup logging handlers
    _setup_console_handler(logger_instance)
    _setup_file_handler(logger_instance, log_location)

    return logger_instance


def _setup_console_handler(logger_instance: logging.Logger) -> None:
    console_handler = logging.StreamHandler()
    logger_instance.addHandler(console_handler)


def _setup_file_handler(logger_instance: logging.Logger, log_location: str) -> None:
    if not os.path.exists(log_location):
        os.makedirs(log_location)

    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # Splitting on the period assuming the user specified `__name__` so we can get the package name
    log_name = logger_instance.name.split('.')[0] + '.log'
    log_file = os.path.join(log_location, log_name)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=DEFAULT_LOG_MAX_BYTES,
        backupCount=DEFAULT_LOG_BACKUP_COUNT,
    )
    file_handler.setFormatter(file_formatter)
    logger_instance.addHandler(file_handler)


def _validate_log_level(log_level: str = 'INFO') -> str:
    log_levels = {
        'CRITICAL': logging.CRITICAL,  # 50
        'ERROR': logging.ERROR,  # 40
        'WARNING': logging.WARNING,  # 30
        'INFO': logging.INFO,  # 20
        'DEBUG': logging.DEBUG,  # 10
        'NOTSET': logging.NOTSET,  # 0
    }

    try:
        active_log_level = log_levels[log_level.upper()]
    except KeyError as error:
        raise KeyError(
            f'Could not setup Woodchips due to invalid log level: {error}, must be one of {log_levels.keys()}'  # noqa
        )

    return active_log_level
