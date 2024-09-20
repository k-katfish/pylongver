from src.longversion import add_longversion_argument
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

def main():
    parser = argparse.ArgumentParser(description='Sample Script')
    add_longversion_argument(parser)
    args = parser.parse_args()
    print("Hello, World!")
    
if __name__ == '__main__':
    main()