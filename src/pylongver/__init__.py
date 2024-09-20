"""
# PyLongVer

A Python package to print the version of the package in a long format with extra
verbose details about the Python interpreter, system, OpenSSL, and all imported
modules whose version information is available.

This package provides a simple interface for printing the version information
by adding an argument to the argparse parser. The package also provides a
function to print the version information directly.

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
"""

from .longversion import LongVersion
from .longversion import add_longversion_argument
from .longversion import print_version_info
from .longversion import get_module_version
