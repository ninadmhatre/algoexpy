__author__ = 'Ninad Mhatre'

from addonpy.IAddonInfo import IAddonInfo
from pylrn.Helper import Common
import pylrn.Helper as Helper


class BubbleSortAddon(IAddonInfo, Common):
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
                   Bubble Sort (Source Wikipedia)
***********************************************************************

Bubble sort, sometimes referred to as sinking sort, is a simple sorting
algorithm that works by repeatedly stepping through the list to be sorted,
comparing each pair of adjacent items and swapping them if they are in
the wrong order. The pass through the list is repeated until no swaps
are needed, which indicates that the list is sorted.
The algorithm gets its name from the way smaller elements "bubble" to the
top of the list. Because it only uses comparisons to operate on elements,
it is a comparison sort.

Although the algorithm is simple, it is too slow for practical use,
even compared to insertion sort

    Data structure :Array

    Worst case performance      : O(n^2)
    Best case performance       : O(n)
    Average case performance    : O(n^2)

    Worst case space complexity : O(1) auxiliary

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

        for idx in range(count):
            self.loop_count += 1
            for inner_idx in range(count - 1 - idx):
                self.loop_count += 1
                if reverse:
                    if data[inner_idx] < data[inner_idx + 1]:
                        data[inner_idx], data[inner_idx + 1] = data[inner_idx + 1], data[inner_idx]  # Swapping
                else:
                    if data[inner_idx] > data[inner_idx + 1]:
                        data[inner_idx], data[inner_idx + 1] = data[inner_idx + 1], data[inner_idx]  # Swapping
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
        return 'BubbleSortAddon'
