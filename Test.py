__author__ = 'Ninad'

from pylrn import AlgorithmsDemo

demo = AlgorithmsDemo()
demo.load(verbose_flag=False)

demo.list_all_algorithms()

bubble_sort = demo.get_instance("BubbleSort")
#bubble_sort.info()
# bubble_sort.print_addon_info()
bubble_sort.show_code()
#bubble_sort.execute([69, 37, 49, 38, 12, 6])
#bubble_sort.execute([6, 12, 37, 38, 49, 69])

#i_sort = demo.get_instance("InsertionSort")
#i_sort.execute([69, 37, 49, 38, 12, 6])
#i_sort.execute([6, 12, 37, 38, 49, 69])

# #
# s_sort = demo.get_instance("SelectionSort")
# s_sort.execute([69, 37, 49, 38, 12, 6])
# s_sort.execute([6, 12, 37, 38, 49, 69])

#s_sort.show_code()

# m_sort = demo.get_instance("MergeSort")
# m_sort.execute([69, 37, 49, 38, 12, 6])
# m_sort.execute([6, 12, 37, 38, 49, 69])

# q_sort = demo.get_instance("QuickSort")
# q_sort.execute([69, 37, 49, 38, 12, 6, 11])
# q_sort.execute([6, 11, 12, 37, 38, 49, 69])

bucket_sort = demo.get_instance("BucketSort")
bucket_sort.execute([69, 37, 49, 38, 12, 6, 11])
bucket_sort.execute([6, 11, 12, 37, 38, 49, 69])