#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import platform
import ssl
import importlib
import argparse

try: import importlib.metadata as importlib_metadata
except ImportError: import pkg_resources

class LongVersion(argparse.Action):
    """
    An argparse action that prints the version information of the Python
    interpreter, system, OpenSSL, and imported modules when called.

    Example:
    
    ```python
    import argparse
    from longversion import LongVersionAction

    parser = argparse.ArgumentParser()
    parser.add_argument('--longversion', action=LongVersionAction, version='1.0.0')
    args = parser.parse_args()
    # When the --longversion argument is called, the version info is printed,
    # along with an extra line showing the version of your program, then exits.
    ```

    This is similar to the built-in `--version` argument in argparse
    (action='version').
    """

    version: str = None
    """
    A program name and/or version to show when the argument is called.
    """

    def __init__(self, option_strings, dest, version: str=None, **kwargs):
        self.version = version
        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        prog = parser.prog
        if self.version:
            if '%(prog)' in self.version:
                self.version = self.version % {'prog': prog}
            else:
                self.version = f"({prog}) {self.version}"
        else:
            self.version = f"({prog})"
        print_version_info(self.version)
        parser.exit()
        
        
def print_version_info(version: str=None) -> None:
    """
    Prints the version information of the Python interpreter, system, OpenSSL,
    and imported modules.
    """
    # Program Version (if provided)
    if version: print(version)
    print("Long Version Info:")

    # Python Version
    print(f"Python Version: {sys.version}")

    # System Details
    print(f"System: {platform.system()}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")
    
    # OpenSSL Version
    print(f"OpenSSL Version: {ssl.OPENSSL_VERSION}")

    # Imported Modules and their Versions
    print("\nImported Modules:")
    for module_name in sorted(sys.modules.keys()):
        if module_name not in ['__main__', 'builtins']:
            if "_" not in module_name and "." not in module_name:
                
                try: version = get_module_version(module_name)
                except: version = 'No version info'
                
                if version != 'No version info': 
                    print(f"{module_name}: {version}")

def get_module_version(module_name):
    """
    Tries to fetch the module version using available implementations.
    
    Args:
        module_name (str): The name of the module.
        
    Returns:
        str: The version of the module
        
    Raises:
        ImportError: If after trying all implementations, no version is found.
    """
    
    try: return importlib_metadata.version(module_name)
    except: pass
    
    try: return pkg_resources.get_distribution(module_name).version
    except: pass
    
    try: return getattr(importlib.import_module(module_name), 
                        '__version__', 'No version info')
    except ImportError: raise ImportError(f"No version info for {module_name}")

# This function makes it easier to add the longversion to argparse
def add_longversion_argument(
    parser: argparse, 
    option: str='--longversion', 
    version: str = None) -> None:
    """
    Adds the longversion argument to the parser.
    
    Args:
        parser (argparse.ArgumentParser): The parser to add the argument to.
        option (str): The option string to use for the argument.
        version (str): The version to show when the argument is called.

    Example:
    
    ```python
    import argparse
    from longversion import add_longversion_argument

    # Example 1
    # Adds the --longversion argument to the parser
    parser = argparse.ArgumentParser()
    add_longversion_argument(parser)
    args = parser.parse_args()
    # When the --longversion argument is called, the version info is printed,
    # and the program exits.

    # Example 2
    # Adds the --version argument to the parser with a custom version of your
    # program
    parser = argparse.ArgumentParser()
    add_longversion_argument(parser, '--version', '1.0.0')
    args = parser.parse_args()
    # When the --version argument is called, the version info is printed,
    # along with an extra line showing the version of your program, then exits.
    ```
    """
    parser.add_argument(option, action=LongVersion, 
         help='Show extended version info and exit')
