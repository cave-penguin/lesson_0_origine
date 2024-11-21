from sort_algorithms.sortfunc import *


from quick_merge import quick_merge
import time

# data_1 = [8, 4, 6, 2, 3, 9, 1, 5, 7]
# data_2 = [1, 4, 3, 12, 5, 6, 7, 4, 3, 9, 0, 6, 68, 34]
# data_3 = [6, 3, 4, 76, 452, 1, 2, 8, 90, 7, 54, 3]

data_1 = create_list()
data_2 = create_list()
data_3 = create_list()

# print(data_1)
# print(data_2)
# print(data_3)

sorted_data1 = sorted(data_1)
sorted_data2 = sorted(data_2)
sorted_data3 = sorted(data_3)


start = time.perf_counter()

merged1 = quick_merge(sorted_data1, sorted_data2)
res = quick_merge(merged1, sorted_data3)
print("Quick Merge: Done")

finish = time.perf_counter()
print("Время работы: " + str((finish - start) * 1000))


start2 = time.perf_counter()

merge_list = sorted(sorted_data1 + sorted_data2 + sorted_data3)
print("Sorted() Merge: Done")

finish2 = time.perf_counter()
print("Время работы: " + str((finish2 - start2) * 1000))
