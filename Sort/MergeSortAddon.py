__author__ = 'Ninad Mhatre'

from addonpy.IAddonInfo import IAddonInfo
import Helper
from Helper import Common


class MergeSortAddon(IAddonInfo, Common):

    pass_cnt, loop_count = 0, 0

    @Helper.MeasureTime
    def execute(self, data, output=True, reverse=False, very_verbose=False):
        """
        Just wrapper around algorithm logic, why such redirection?
        try it out it will be fun...
        """
        self.log("{0} >> Before Sorting   : {1}".format(self.__addon__(), data), output)
        self.log(Helper.insert_separator(), very_verbose)

        self.logic(data, output, reverse, very_verbose)

        self.log(Helper.insert_separator(), very_verbose)
        self.log("{0} >> After Sorting    : {1}".format(self.__addon__(), data), output)
        self.log("{0} >> Total Loop Count : {1}".format(self.__addon__(), self.loop_count), output)

    def info(self):
        """
        Copied paragraph from Wikipedia about algorithm, incase user wants
        to know very basic about algorithm.
        """

        print("""
***********************************************************************
                   Merge Sort (Source Wikipedia)
***********************************************************************

Merge Sort (also commonly spelled mergesort) is an O(n log n) comparison-based
sorting algorithm. Most implementations produce a stable sort, which means
that the implementation preserves the input order of equal elements in the
sorted output. Mergesort is a divide and conquer algorithm that was invented
by John von Neumann in 1945.

    Data structure :Array

    Worst case performance      : O(n log n)
    Best case performance       : O(n log n) typical / O(n) natural
    Average case performance    : O(n log n)

    Worst case space complexity : O(n) auxiliary

>> Note: For Full article, run .info_online()

***********************************************************************
        """)

    def logic(self, data, output, reverse, very_verbose):
        """
        Algorithm logic
        :param data: Array to be sorted
        :return: Sorted array
        """
        self.pass_cnt += 1

        count = len(data)
        if count > 1:
            mid = count / 2

            left_array = data[0:mid]
            right_array = data[mid:]

            self.logic(left_array, output, reverse, very_verbose)
            self.logic(right_array, output, reverse, very_verbose)

            left_idx, right_idx = 0, 0

            for idx in range(count):
                self.loop_count += 1
                if left_idx < len(left_array):
                    left_val = left_array[left_idx]
                else:
                    left_val = None

                if right_idx < len(right_array):
                    right_val = right_array[right_idx]
                else:
                    right_val = None

                if reverse:
                    if (left_val is not None and right_val is not None and left_val > right_val) or right_val is None:
                        data[idx] = left_val
                        left_idx += 1
                    elif (left_val is not None and right_val is not None and right_val >= left_val) or left_val is None:
                        data[idx] = right_val
                        right_idx += 1
                    else:
                        raise IndexError("Failed to sort 2 arrays!")
                else:
                    if (left_val is not None and right_val is not None and left_val < right_val) or right_val is None:
                        data[idx] = left_val
                        left_idx += 1
                    elif (left_val is not None and right_val is not None and right_val <= left_val) or left_val is None:
                        data[idx] = right_val
                        right_idx += 1
                    else:
                        raise IndexError("Failed to sort 2 arrays!")
        self.log_v(" Pass #{0:02d} : {1}".format(self.pass_cnt, data), very_verbose)
        return data

    def info_online(self):
        """
        First good use of HELP_URL in addonpy template
        :return: Opens the Help URL in default browser
        """
        url = self.get_help_url()
        print("Opening URL '{0}'".format(url))
        Helper.open_url(url)

    def show_code(self):
        """
        Print algorithm logic to terminal.
        """
        self.show_source()

    @staticmethod
    def __addon__():
        return 'MergeSortAddon'