
__author__ = '<Please Specify Author>'

from addonpy.IAddonInfo import IAddonInfo
from pylrn.Helper import Common
import pylrn.Helper as Helper


class StackDSAddon(IAddonInfo):
    def info(self):
        raise NotImplemented

    def execute(self):
        pass

    def logic(self):
        raise NotImplemented

    def info_online(self):
        raise NotImplemented

    def show_code(self):
        raise NotImplemented

    @staticmethod
    def __addon__():
        return 'StackDSAddon'
