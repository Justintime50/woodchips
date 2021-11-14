# CHANGELOG

## v0.1.1 (2021-11-13)

* Changed the name of the log files from `woodchips.log` to the `logger_name` passed in by the user (we have logic to deconstruct `__name__` if that is passed in)

## v0.1.0 (2021-11-13)

* Initial release
* Setup logging to console and file with a consistent and reliable interface. Create logger instances with customizable logger names, log locations, and log level
