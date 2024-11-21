import random
import time
import heapq


# nums = [6, 7, 4, 8, 9, 2, 5]
def create_list():
    nums = []
    for _ in range(5):
        nums.append(random.randint(1, 9))
    return nums


# print(num s)


# start = time.perf_counter()


def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    # else:
    #     return "Bubble sort: Done"
    return ls


# print(bubble_sort(create_list()))


# finish = time.perf_counter()
# print("Время работы: " + str((finish - start) * 1000))

# start1 = time.perf_counter()


def selection_sort(ls):
    # print(ls)
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    # return "Selection sort: Done"
    return ls


# print(selection_sort(create_list()))


# finish1 = time.perf_counter()
# print("Время работы: " + str((finish1 - start1) * 1000))

# start8 = time.perf_counter()


def insertion_sort(ls):
    # print(ls)
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


# print(insertion_sort(create_list()))

# finish8 = time.perf_counter()
# print("Время работы: " + str((finish8 - start8) * 1000))


# start2 = time.perf_counter()
#
#
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# print(merge_sort(create_list()))


#
#
# # Example usage
#
# sorted_arr = merge_sort(nums)
# if sorted_arr:
#     print("Merge sort: Done")
#
#
# finish2 = time.perf_counter()
# print("Время работы: " + str((finish2 - start2) * 1000))
#
#
# start3 = time.perf_counter()
#
#
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


#
#
# # Example usage
#
# sorted_arr = quick_sort(create_list())
# if sorted_arr:
#     print(sorted_arr)
#     print("Quick sort: Done")
#
#
# finish3 = time.perf_counter()
# print("Время работы: " + str((finish3 - start3) * 1000))
#
#
# start5 = time.perf_counter()
#


def heap_sort(arr):
    # Create a max heap
    heap = [-x for x in arr]
    heapq.heapify(heap)

    # Extract the sorted elements one by one
    sorted_arr = []
    while heap:
        sorted_arr.append(-heapq.heappop(heap))

    return arr


#
#
# # Example usage
# sorted_arr = heap_sort(nums)
# print(sorted_arr)
#
# finish5 = time.perf_counter()
# print("Время работы: " + str((finish5 - start5) * 1000))
#
# start6 = time.perf_counter()
#
#
def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    num_digits = len(str(abs(max_num)))

    # Perform counting sort for each digit
    for i in range(num_digits):
        buckets = [0] * 10
        for num in arr:
            digit = (num // 10**i) % 10
            buckets[digit] += 1
        arr = []
        for j in range(10):
            for _ in range(buckets[j]):
                arr.append(j * 10**i)

    return arr


#
# # Example usage
#
# sorted_arr = radix_sort(nums)
# print(sorted_arr)
#
# finish6 = time.perf_counter()
# print("Время работы: " + str((finish6 - start6) * 1000))
#
# start7 = time.perf_counter()
#
#
def counting_sort(arr, k):
    n = len(arr)
    count = [0] * (k + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Calculate the cumulative sum of counts
    for i in range(1, k + 1):
        count[i] += count[i - 1]

    # Build the sorted array
    sorted_arr = [0] * n
    for num in reversed(arr):
        index = count[num] - 1
        sorted_arr[index] = num
        count[num] -= 1

    return arr


#
#
# # Example usage
# sorted_arr = counting_sort(nums, max(nums))
# print(sorted_arr)
#
# finish7 = time.perf_counter()
# print("Время работы: " + str((finish7 - start7) * 1000))
#
#
# start4 = time.perf_counter()
# sorted_nums = nums.sort()
# print("Sort(): Done")
#
#
# finish4 = time.perf_counter()
# print("Время работы: " + str((finish4 - start4) * 1000))
