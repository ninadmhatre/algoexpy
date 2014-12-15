__author__ = 'Ninad'

from addonpy.IAddonInfo import IAddonInfo
import Helper
from Helper import Common


class QuickSortAddon(IAddonInfo, Common):
    loop_count, pass_cnt = 0, 0

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
                   Quick Sort (Source Wikipedia)
***********************************************************************

Quicksort, or partition-exchange sort, is a sorting algorithm developed
by Tony Hoare that, on average, makes O(n log n) comparisons to sort n
items. In the worst case, it makes O(n2) comparisons, though this behavior
is rare. Quicksort is often faster in practice than other O(n log n)
algorithms.[1] Additionally, quicksort's sequential and localized memory
references work well with a cache. Quicksort is a comparison sort and,
in efficient implementations, is not a stable sort. Quicksort can be
implemented with an in-place partitioning algorithm, so the entire sort
can be done with only O(log n) additional space used by the stack
during the recursion.[2]

    Data structure :Array

    Worst case performance      : O(n^2)
    Best case performance       : O(n log n) typical / O(n) 3-way
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
            pivot = count / 2

            smaller = list()
            larger = list()
            pivot_elem = data[pivot]

            for idx, elem in enumerate(data):
                self.loop_count += 1
                if idx != pivot:
                    if elem < pivot_elem:
                        smaller.append(elem)
                    else:
                        larger.append(elem)

            self.logic(smaller, output, reverse, very_verbose)
            self.logic(larger, output, reverse, very_verbose)

            if reverse:
                data[:] = larger + [pivot_elem] + smaller
            else:
                data[:] = smaller + [pivot_elem] + larger

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
        return 'QuickSortAddon'