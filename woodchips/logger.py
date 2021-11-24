import logging
import logging.handlers
import os

# 200kb * 5 files = 1mb of logs
DEFAULT_LOG_MAX_BYTES = 200000  # 200kb
DEFAULT_LOG_BACKUP_COUNT = 5


class Logger:
    def __init__(self, name: str, level: str = 'INFO'):
        """Setup a logger based on a provided set of input.

        - name: Each module that requires logging should instantiate a new class and pass a
        new name based on the module using logging. Typically for most purposes, this
        should be `__name__` passed as `name` or the name of your package.
        - level: Every logger needs a level. Logged messages of a greater or equal value
        to the log level will be shown.
        - logger: This is the actual `logging.Logger` object wrapped on `woodchips.Logger`,
        call your logging actions on this property such as `info()` or `warning()`.
        """
        self.name = name
        self.level = level
        self.logger = get(self.name)

        log_level = self._validate_log_level()
        self.logger.setLevel(log_level)

    def log_to_console(self, formatter: str = '%(message)s') -> None:
        """Adds a console handler to a logger."""
        console_handler = logging.StreamHandler()

        console_formatter = logging.Formatter(formatter)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

    def log_to_file(
        self,
        location: str,
        formatter: str = '%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
        log_size: int = DEFAULT_LOG_MAX_BYTES,
        num_of_logs: int = DEFAULT_LOG_BACKUP_COUNT,
    ) -> None:
        """Adds a file handler to a logger."""
        if not os.path.exists(location):
            os.makedirs(location)

        # Splitting on the period assuming the user specified `__name__`
        # so we can get the root package name for log filenames.
        log_name = self.logger.name.split('.')[0] + '.log'
        log_file = os.path.join(location, log_name)

        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=log_size,
            backupCount=num_of_logs,
        )

        file_formatter = logging.Formatter(formatter)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def _validate_log_level(self) -> int:
        """Internal utility to validate the input log level is valid, raise an error if not."""
        log_levels = {
            'CRITICAL': logging.CRITICAL,  # 50
            'ERROR': logging.ERROR,  # 40
            'WARNING': logging.WARNING,  # 30
            'INFO': logging.INFO,  # 20
            'DEBUG': logging.DEBUG,  # 10
            'NOTSET': logging.NOTSET,  # 0
        }

        try:
            log_level = log_levels[self.level.upper()]
        except KeyError as error:
            raise KeyError(
                f'Could not setup Woodchips due to invalid log level: {error}, must be one of {log_levels.keys()}'  # noqa
            )

        return log_level


def get(logger_name: str) -> logging.Logger:
    """Gets a logger instance by name."""
    logger = logging.getLogger(logger_name)

    return logger
