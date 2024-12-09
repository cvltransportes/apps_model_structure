import os
import sys
from dataprocess import dataprocessing as hd

from settings import (
    PATH_DOWNLOADS
)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def process_something_here():
    """Only a single example to use dataprocess"""
    table = hd.import_file(PATH_DOWNLOADS)
    table = hd.clear_table(table)
    table = hd.convert_table_types(table)
    print(table)
    return table
