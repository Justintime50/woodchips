# CHANGELOG

## v0.2.0 (2021-11-23)

* Completely refactored the app to use a `Logger` class for better granularity and control over the configuration of each logger instance.
* Added `log_to_console` method
* Added `log_to_file` method
* Added `get` function to retrieve a logger instance by name
* Allow users to specify the `formatter` on either the console or file handler
* Allow users to specify the `num_of_logs` and `log_size` when logging to a file
* Various improvements, bug fixes, and stronger tests

## v0.1.1 (2021-11-13)

* Changed the name of the log files from `woodchips.log` to the `logger_name` passed in by the user (we have logic to deconstruct `__name__` if that is passed in)

## v0.1.0 (2021-11-13)

* Initial release
* Setup logging to console and file with a consistent and reliable interface. Create logger instances with customizable logger names, log locations, and log level
 