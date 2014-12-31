__author__ = 'Ninad'

from addonpy.IAddonInfo import IAddonInfo
from pylrn.Helper import Common
import pylrn.Helper as Helper


class InsertionSortAddon(IAddonInfo, Common):
    loop_count = 0

    @Helper.MeasureTime
    def execute(self, data, output=True, reverse=False, very_verbose=False):
        """
        Just wrapper around algorithm logic, why such redirection?
        try it out it will be fun...
        """
        self.log("{0} >> Before Sorting   : {1}".format(self.__addon__(), data), output)
        self.log(Helper.insert_separator(), very_verbose)
        self.loop_count = 0

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
                   Insertion Sort (Source Wikipedia)
***********************************************************************

Insertion sort is a simple sorting algorithm that builds the final sorted
array (or list) one item at a time. It is much less efficient on large
lists than more advanced algorithms such as quicksort, heapsort,
or merge sort. However, insertion sort provides several advantages:

* Simple implementation
* Efficient for (quite) small data sets
* More efficient in practice than most other simple quadratic (i.e., O(n2))
  algorithms such as selection sort or bubble sort
* Adaptive, i.e., efficient for data sets that are already substantially sorted:
  the time complexity is O(nk) when each element in the input is no more than
  k places away from its sorted position
* Stable; i.e., does not change the relative order of elements with equal keys
* In-place; i.e., only requires a constant amount O(1) of additional memory space
* Online; i.e., can sort a list as it receives it

    Data structure :Array

    Worst case performance      : O(n^2)
    Best case performance       : O(n) comparisons, O(1) swaps
    Average case performance    : O(n^2) comparisons, swaps

    Worst case space complexity : O(n) total, O(1) auxiliary

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

        for idx in range(1, count):
            self.loop_count += 1
            inner_idx = idx
            if reverse:
                while inner_idx > 0 and data[inner_idx] > data[inner_idx - 1]:
                    self.loop_count += 1
                    data[inner_idx], data[inner_idx - 1] = data[inner_idx - 1], data[inner_idx]
                    inner_idx -= 1
            else:
                while inner_idx > 0 and data[inner_idx] < data[inner_idx - 1]:
                    self.loop_count += 1
                    data[inner_idx], data[inner_idx - 1] = data[inner_idx - 1], data[inner_idx]
                    inner_idx -= 1
            self.log_v(" >> Pass #{0:02d} : {1}".format(idx, data), very_verbose)
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
        return 'InsertionSortAddon'
