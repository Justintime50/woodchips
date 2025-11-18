# CHANGELOG

## v2.0.0 (2025-11-18)

- Drops support for Python 3.8 and 3.9
- Bumps deps

## v1.0.0 (2023-07-01)

- Drops support for Python 3.7

## v0.2.4 (2022-04-19)

- Small improvements to code, documentation, and releasing process

## v0.2.3 (2021-11-29)

- Adds a `py.typed` file for `mypy` type checking
- Adds `mypy` as a dev dependency

## v0.2.2 (2021-11-25)

- Makes the previously exposed `logger` class variable private as it was intended to remain internal and not be exposed

## v0.2.1 (2021-11-23)

- Changed the order of the default file formatter to show level before function name for easier scanning of log files

## v0.2.0 (2021-11-23)

- Completely refactored the app to use a `Logger` class for better granularity and control over the configuration of each logger instance.
- Added `log_to_console` method
- Added `log_to_file` method
- Added `get` function to retrieve a logger instance by name
- Allow users to specify the `formatter` on either the console or file handler
- Allow users to specify the `num_of_logs` and `log_size` when logging to a file
- Various improvements, bug fixes, and stronger tests

## v0.1.1 (2021-11-13)

- Changed the name of the log files from `woodchips.log` to the `logger_name` passed in by the user (we have logic to deconstruct `__name__` if that is passed in)

## v0.1.0 (2021-11-13)

- Initial release
- Setup logging to console and file with a consistent and reliable interface. Create logger instances with customizable logger names, log locations, and log level
