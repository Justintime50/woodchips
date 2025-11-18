<div align="center">

# Woodchips

The cutest little logger you've ever seen.

[![Build Status](https://github.com/Justintime50/woodchips/workflows/build/badge.svg)](https://github.com/Justintime50/woodchips/actions)
[![Coverage Status](https://img.shields.io/codecov/c/github/justintime50/woodchips)](https://app.codecov.io/github/Justintime50/woodchips)
[![PyPi](https://img.shields.io/pypi/v/woodchips)](https://pypi.org/project/woodchips)
[![Licence](https://img.shields.io/github/license/Justintime50/woodchips)](LICENSE)

<img src="https://raw.githubusercontent.com/Justintime50/assets/main/src/woodchips/showcase.png" alt="Showcase">

</div>

> Aren't logs just a bunch of woodchips?

Woodchips was created to be the cutest little logger you've ever seen. I wanted something dead simple and reusable as I found myself using the same logging setup over and over in projects. Woodchips gives you everything you need to setup the Python logging library in your project, all without the need to import or call on the `logging` package, know the various syntaxes for setting up handlers and formatters, etc which makes logging with Woodchips incredibly simple and clean.

## Install

```bash
# Install tool
pip3 install woodchips

# Install locally
just install
```

## Usage

- A `Logger` instance must be created to use Woodchips. Simply specify a name and logging level, tell Woodchips where to log items (console and/or files), and start chipping away!
- Need multiple loggers, no problem. Spin up separate `Logger` instances for your needs. Maybe you need a console logger for certain output that requires a specific format while another module needs a generic file formatter. Woodchips makes it easy to setup and configure all your loggers.
- **Logging to a file:** Woodchips will automatically roll over your log files once it reaches the `log_size`. You can configure `num_of_logs` to specify how many log files will be kept in the rotation.
  - **NOTE:** Woodchips has a very small default log size of just `200kb` with `5` log files for a total of `1mb` of logs. For production applications, these values may need to be drastically increased.
- **Formatters:** You can configure the format of log files per handler (console and/or files); however, defaults are set (and shown below) if you just need basic logging.

### Setting up Woodchips

```python
import woodchips

# Setup a new logger instance
logger = woodchips.Logger(
    name='my_logger_name',  # The name of your logger instance, often will be `__name__`
    level='INFO',  # The log level you want to use
)

# Setup console logging
logger.log_to_console(formatter='%(message)s')

# Setup file logging
logger.log_to_file(
    location='path/to/log_files',
    formatter='%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
    log_size=200000,  # Size of a single file in bytes
    num_of_logs=5,  # Number of log files to keep in the rotation
)
```

### Using Woodchips

```python
import woodchips

# Retrieve a logger instance by name (assumes it's already been created)
logger = woodchips.get('my_logger_name')

# Log a message (will be logged to console and a file based on the example from above)
logger.info('This is how to setup Woodchips!')
```

### Logger Levels

- CRITICAL
- ERROR
- WARNING
- INFO
- DEBUG
- NOTSET

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
