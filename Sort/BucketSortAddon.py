__author__ = 'Ninad Mhatre'

from addonpy.IAddonInfo import IAddonInfo
import Helper
from addonpy.addonpy import AddonLoader
import math
from Helper import Common


class BucketSortAddon(IAddonInfo, Common):
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
                   Bucket Sort (Source Wikipedia)
***********************************************************************

Bucket sort, or bin sort, is a sorting algorithm that works by partitioning
an array into a number of buckets. Each bucket is then sorted individually,
either using a different sorting algorithm, or by recursively applying the
bucket sorting algorithm. It is a distribution sort, and is a cousin of
radix sort in the most to least significant digit flavour. Bucket sort is
a generalization of pigeonhole sort. Bucket sort can be implemented with
comparisons and therefore can also be considered a comparison sort algorithm.
The computational complexity estimates involve the number of buckets.

Bucket sort works as follows:

1. Set up an array of initially empty "buckets".
2. Scatter: Go over the original array, putting each object in its bucket.
3. Sort each non-empty bucket.
4. Gather: Visit the buckets in order and put all elements back into the original array.


    ** k : Number of buckets used.

    Data structure              : Array

    Worst case performance      : O(n^2)
    Best case performance       : O(n + k)
    Average case performance    : O(n + k)

    Worst case space complexity : O(n * k)

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

        bucket_list = [list() for _ in range(count)]
        biggest = data[0]
        for i in range(1, count):
            if biggest < data[i]:
                biggest = data[i]

        divisor = self.divide_to_get_int(biggest, count, to_floor=False)

        for idx in range(count):
            self.loop_count += 1
            new_idx = self._get_index(data[idx], divisor)
            bucket_list[new_idx].append(data[idx])

        #
        # Assuming insertion sort is already loaded..
        #

        insertion_sort = AddonLoader.get_loaded_addon_instance("InsertionSortAddon")

        j = 0
        if reverse:
            first = len(bucket_list) - 1
            last = -1
            step = -1
        else:
            first = 0
            last = len(bucket_list)
            step = 1

        for b_idx in range(first, last, step):
            if insertion_sort is not None:
                insertion_sort.execute(bucket_list[b_idx], reverse=reverse, output=False, very_verbose=False)
            else:
                bucket_list[b_idx].sort(reverse=reverse)

            for i in range(len(bucket_list[b_idx])):
                data[j] = bucket_list[b_idx][i]
                j += 1

        return data

    def _get_index(self, value, denominator):
        return self.divide_to_get_int(value, denominator, to_floor=True)

    def divide_to_get_int(self, number, divisor, to_floor=False):
        """
        Why 'float(denominator)'? try out simple division in py2 & py 3
        you will notice the difference! Its painful...
        :param number: number to be divided
        :param divisor: ?
        :param to_floor: decimals converted to integer, 6.9 -> 6, 9.9 -> 9
                         otherwise, 7.1 -> 8, 8.5 -> 9
        :return: math ceil converted to int
        """
        if to_floor:
            return int(math.floor(number / float(divisor)))
        else:
            return int(math.ceil(number / float(divisor)))

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
        return 'BucketSortAddon'