import os
import sys
from dataprocess import dataprocessing as hd

from settings import *
import src.dataprocessing as dp
import src.webscrapping as wb

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def task1():
    """Gather all workflow to perform task1"""
    with wb.MyBot() as mb:
        mb.init_browser(headless=False, browser="firefox")
        mb.open(
            "https://github.com/login"
        )
        mb.login()
        # more actions ...
        # download something to PATH_DOWNLOADS...


def task2():
    """Gather all workflow to perform task2"""
    return dp.process_something_here()
