<div align="center">

# Woodchips

The cutest little logger you've ever seen.

[![Build Status](https://github.com/Justintime50/woodchips/workflows/build/badge.svg)](https://github.com/Justintime50/woodchips/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/woodchips/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/woodchips?branch=main)
[![PyPi](https://img.shields.io/pypi/v/woodchips)](https://pypi.org/project/woodchips)
[![Licence](https://img.shields.io/github/license/Justintime50/woodchips)](LICENSE)

<img src="https://raw.githubusercontent.com/Justintime50/assets/main/src/woodchips/showcase.png" alt="Showcase">

</div>

> All logs are made up of woodchips

I found myself using the same logging setup logic over and over in projects so I decided to pull it out into its own little package. Woodchips gives you everything you need to setup the Python logging library in your project, all without the need to import or call on the `logging` package making logging incredibly simple and clean.

**NOTE:** Woodchips currently assumes you want to print logs to console in addition to saving to a file. In the future, this may be configurable.

## Install

```bash
# Install tool
pip3 install woodchips

# Install locally
make install
```

## Usage

```python
import woodchips


logger = woodchips.setup(
    logger_name=__name__,  # Should be the name of your module
    logger_location='my_path',
    logger_level='INFO'
)

logger.info('This is how to setup Woodchips!')
logger.warning('Pass any string to log, set the lowercase logger level on invocation')
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
