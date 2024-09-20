# PyLongVer

PyLongVer is a utility to print a long version message about your python code.

This prints the version of the package in a long format with extra verbose
details about the Python interpreter, system, OpenSSL, and all imported modules
whose version information is available.

This package provides a simple interface for printing the version information
by adding an argument to the argparse parser. The package also provides a
function to print the version information directly.

## Sample output

```python
>>> from pylongver import print_version_info
>>> print_version_info()
Python Version: 3.12.6 (main, Sep  8 2024, 13:18:56) [GCC 14.2.1 20240805]
System: Linux
Platform: Linux-6.10.10-arch1-1-x86_64-with-glibc2.40
Architecture: ('64bit', 'ELF')
OpenSSL Version: OpenSSL 3.3.2 3 Sep 2024

Imported Modules:
argparse: 1.1
csv: 1.0
platform: 1.0.8
pylongver: 0.1.0
re: 2.2.1
zlib: 1.0
```

## Usage

### Using the ArgumentParser

```python
import argparse
from pylongver import add_longversion_argument

parser = argparse.ArgumentParser()
add_longversion_argument(parser)
args = parser.parse_args()
```

### Using the print_version_info function

```python
from pylongver import print_version_info

print_version_info()
```

## About

### Authors

Kyle Ketchell, creator and maintainer

### License

MIT
