<div align="center">

# Woodchips

The cutest little logger you've ever seen.

[![Build Status](https://github.com/Justintime50/woodchips/workflows/build/badge.svg)](https://github.com/Justintime50/woodchips/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/woodchips/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/woodchips?branch=main)
[![PyPi](https://img.shields.io/pypi/v/woodchips)](https://pypi.org/project/woodchips)
[![Licence](https://img.shields.io/github/license/Justintime50/woodchips)](LICENSE)

<img src="https://raw.githubusercontent.com/Justintime50/assets/main/src/woodchips/showcase.png" alt="Showcase">

</div>

> Aren't logs just a bunch of woodchips?

I found myself using the same logging setup logic over and over in projects so I decided to pull it out into its own little package. Woodchips gives you everything you need to setup the Python logging library in your project, all without the need to import or call on the `logging` package making logging incredibly simple and clean.

## Install

```bash
# Install tool
pip3 install woodchips

# Install locally
make install
```

## Usage

* A `Logger` instance must be created to use Woodchips. Simply specify a name and logging level, tell Woodchips where to log items (console and/or files), and start chipping away!
* Need multiple loggers, no problem. Spin up separate `Logger` instances for your needs. Maybe you need a console logger for certain output that requires a specific format while another module needs a generic file formatter. Woodchips makes it simple to setup and configure all your loggers.
* **Logging to a file:** Woodchips will automatically roll over your log files once it reaches the `log_size`. You can configure `num_of_logs` to specify how many log files will be kept in the rotation.
* **Formatters:** You can configure the format of log files per handler (console and/or files); however, defaults are set (and shown below) if you just need basic logging.

```python
import woodchips


# Setup a new logger instance
my_logger = woodchips.Logger(
    name=__name__,  # Should be the name of your package
    level='INFO',  # The log level you want to use
)

# Setup console logging
my_logger.log_to_console(formatter='%(message)s')

# Setup file logging
my_logger.log_to_file(
    location='path/to/log_files',
    formatter='%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
    log_size=500000,  # Size of a single file in bytes
    num_of_logs=10,  # Number of log files to keep in the rotation
)

# Log a message (will be logged to console and a file based on the config above)
my_logger.logger.info('This is how to setup Woodchips!')
```

### Logger Levels

* CRITICAL
* ERROR
* WARNING
* INFO
* DEBUG
* NOTSET

## Development

```bash
# Get a comprehensive list of development tools
make help
```
