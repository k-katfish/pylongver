#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib.metadata
import sys
import platform
import ssl
import importlib
import argparse

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import pkg_resources

class LongVersionAction(argparse.Action):
    def __init__(self, option_strings, dest, **kwargs):
        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print_version_info()
        parser.exit()
        
        
def print_version_info():
    """
    Prints the version information of the Python interpreter, system, OpenSSL,
    and imported modules.
    """
    
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
def add_longversion_argument(parser):
    parser.add_argument('--lvi', '--longversion', action=LongVersionAction, 
                        help='Show extended version info and exit')

