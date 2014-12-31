__author__ = 'Ninad'

import webbrowser
import os
import sys
import inspect
from datetime import datetime
import random


def open_url(url):
    if url is not None:
        webbrowser.open_new_tab(url)


def generate_sequence(start, end, length):
    return [random.randint(start, end) for un_used in range(length)]


def insert_separator():
    return "-" * 40


def MeasureTime(func):
    def measure(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()

        if kwargs.get('very_verbose'):
            print("Time Taken (micro-sec) : {0}".format((end_time - start_time).microseconds))
            print("Total Element          : {0}".format(len(args[1])))

    return measure


class Common(object):
    def __init__(self):
        pass

    def show_source(self):
        try:
            source = inspect.getsource(self.logic).split('\n')
        except IOError:
            print("Failed to read the source of '{0}' algorithm".format(self.__addon__))
        except ImportError:
            print("Failed to read the source of '{0}' algorithm".format(self.__addon__))
        else:
            print("\n---------------- Sorting Logic For : [{0}] -----------------\n".format(self.__addon__()))
            for line in source:
                print(line)
            print("\n")

    def log(self, msg, verbose):
        if verbose:
            print(msg)

    def log_v(self, msg, verbose):
        if verbose:
            print(msg)