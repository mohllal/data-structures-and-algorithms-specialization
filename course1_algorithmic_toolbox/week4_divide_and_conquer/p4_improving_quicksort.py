# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# To force the given implementation of the quick sort algorithm to efficiently process sequences with few unique elements.
# The goal of this task is to replace a 2-way partition with a 3-way partition. 
# That is, the new partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.

import random

# O(n)
def two_way_partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            (a[i], a[j]) = (a[j], a[i])

    (a[i + 1], a[high]) = (a[high], a[i + 1])
    return i + 1

# O(1)
def two_way_random_pivot_partitioning(a, low, high):
    randpivot = random.randrange(low, high)
 
    a[high], a[randpivot] = a[randpivot], a[high]
    return two_way_partition(a, low, high)

# O(n log n)
def two_way_quick_sort(a, low, high):
   if low < high:
       # pi = partition(a, low, high)
       pi = two_way_random_pivot_partitioning(a, low, high)

       two_way_quick_sort(a, low, pi - 1)
       two_way_quick_sort(a, pi + 1, high)

# O(n)
def three_way_partition(a, low, high):
    lt = low  # We initiate lt to be the part that is less than the pivot
    i = low   # We scan the array from left to right
    gt = high  # The part that is greater than the pivot
    pivot = a[high]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt

# O(1)
def three_way_random_pivot_partitioning(a, low, high):
    randpivot = random.randrange(low, high)
 
    a[high], a[randpivot] = a[randpivot], a[high]
    return three_way_partition(a, low, high)

# O(n log n)
def three_way_quick_sort(a, low, high):
    if low < high:
       lt, gt = three_way_random_pivot_partitioning(a, low, high)

       three_way_quick_sort(a, low, lt - 1)
       three_way_quick_sort(a, gt + 1, high)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
     
    # two_way_quick_sort(a, 0, n - 1)
    three_way_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')