__author__ = 'Ninad'

from algoexpy import AlgorithmsDemo

demo = AlgorithmsDemo()
demo.load(verbose_flag=False)

#demo.list_all_algorithms()

#bubble_sort = demo.get_instance("BubbleSort")
#bubble_sort.info()
# bubble_sort.print_addon_info()
# bubble_sort.show_code()
#bubble_sort.execute([69, 37, 49, 38, 12, 6])

#i_sort = demo.get_instance("InsertionSort")
# i_sort.execute([69, 37, 49, 38, 12, 6], reverse=False)
# #
# s_sort = demo.get_instance("SelectionSort")
# s_sort.execute([69, 37, 49, 38, 12, 6])
#s_sort.show_code()

#m_sort = demo.get_instance("MergeSort")
#m_sort.execute([69, 37, 49, 38, 12, 6])

#q_sort = demo.get_instance("QuickSort")
#q_sort.execute([69, 37, 49, 38, 12, 6], reverse=False)

bucket_sort = demo.get_instance("BucketSort")
bucket_sort.execute([69, 37, 49, 38, 12, 6], reverse=False)