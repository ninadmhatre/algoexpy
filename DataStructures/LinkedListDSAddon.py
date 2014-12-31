
__author__ = '<Please Specify Author>'

from addonpy.IAddonInfo import IAddonInfo
from pylrn.Helper import Common
import pylrn.Helper as Helper


class LinkedListDSAddon(IAddonInfo):
    def start(self):
        raise NotImplemented

    def stop(self):
        raise NotImplemented

    def execute(self):
        raise NotImplemented

    @staticmethod
    def __addon__():
        return 'LinkedListDSAddon'
