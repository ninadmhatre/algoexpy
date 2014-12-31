__author__ = 'Ninad'

from addonpy.IAddonInfo import IAddonInfo
import Helper
from Helper import Common


class SelectionSortAddon(IAddonInfo, Common):
    loop_count = 0

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
                   Selection Sort (Source Wikipedia)
***********************************************************************

In computer science, selection sort is a sorting algorithm, specifically
an in-place comparison sort. It has O(n2) time complexity, making it
inefficient on large lists, and generally performs worse than the similar
insertion sort. Selection sort is noted for its simplicity, and it has
performance advantages over more complicated algorithms incertain
situations, particularly where auxiliary memory is limited.

The algorithm divides the input list into two parts: the sublist of items
already sorted, which is built up from left to right at the front (left)
of the list, and the sublist of items remaining to be sorted that occupy
the rest of the list. Initially, the sorted sublist is empty and the
unsorted sublist is the entire input list. The algorithm proceeds by finding
the smallest (or largest, depending on sorting order) element in the unsorted
sublist, exchanging it with the leftmost unsorted element
(putting it in sorted order), and moving the sublist boundaries one element
to the right.

    Data structure              : Array

    Worst case performance      : O(n^2)
    Best case performance       : O(n^2)
    Average case performance    : O(n^2)

    Worst case space complexity : O(n)

>> Note: For Full article, run .info_online()

***********************************************************************
        """)

    def logic(self, data, output=True, reverse=False, very_verbose=False):
        """
        Algorithm logic
        :param data: Array to be sorted
        :param output: Show output or not
        :param reverse: Sort in reverse
        :return: Sorted array
        """
        count = len(data)

        # find the min element from 1..n and put at 1st position
        # then 2..n and 2nd position
        # so on...

        for idx in range(count):
            self.loop_count += 1
            min_element = self.find_min_element(data, idx, count, reverse)
            data[idx], data[min_element] = data[min_element], data[idx]
            self.log_v(" >> Pass #{0:02d} : {1}".format(idx, data), very_verbose)

        return data

    def find_min_element(self, data, start_idx, end_idx, reverse=False):
        element_index = start_idx

        for i in range(start_idx, end_idx):
            self.loop_count += 1
            if reverse:
                if data[element_index] < data[i]:
                    element_index = i
            else:
                if data[element_index] > data[i]:
                    element_index = i
        return element_index

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
        return 'SelectionSortAddon'
