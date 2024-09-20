import argparse
import numpy
import pandas
import matplotlib
import seaborn
import sklearn
import datetime
import itsdangerous
import click
import blinker
import six

from pylongver import LongVersion

def main():
    parser = argparse.ArgumentParser(description='Sample Script')
    parser.add_argument('--version', action=LongVersion, version="1.0")
    parser.add_argument('--prog-version', action=LongVersion, version="%(prog)s 1.0")
    parser.add_argument('--sample-version', action=LongVersion, version="Sample 1.0")
#    add_longversion_argument(parser)
    args = parser.parse_args()
    print("Hello, World!")
    
if __name__ == '__main__':
    main()
