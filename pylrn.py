from __future__ import print_function

__author__ = 'Ninad'

from addonpy.addonpy import AddonLoader
import os


class AlgorithmsDemo(object):
    def __init__(self):
        self.loader = None
        self.search_dirs = list()
        self.search_dirs.append(os.path.dirname(__file__))

    def add_search_dirs(self, search_dirs):
        """
        Append to existing search locations
        :param search_dirs: list of additional search locations
        """
        [self.search_dirs.append(_dir) for _dir in search_dirs if os.path.isdir(_dir)]

    def load(self, verbose_flag):
        """
        Load algorithms using addonpy module
        :param verbose_flag: make it verbose?
        """
        self.loader = AddonLoader(verbose=verbose_flag, recursive=True)
        self.loader.set_addon_methods(["execute", "info", "logic", "info_online", "show_code", "__addon__"])
        self.loader.set_addon_dirs(self.search_dirs)
        self.loader.load_addons()

    def get_instance(self, algorithm):
        """
        Get instance of addon by name
        :param algorithm: name of addon / algorithm
        :return: instance of algorithm addon
        """
        if not algorithm.endswith("Addon"):
            algorithm += "Addon"
        return self.loader.get_instance(algorithm)

    def list_all_algorithms(self, by_type=None):
        if by_type is None:
            [print(_addon) for _addon in self.loader.get_loaded_addons(list_all=True)]
        else:
            [print(_addon) for _addon in self.loader.get_loaded_addons(by_type=by_type)]