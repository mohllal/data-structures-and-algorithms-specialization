# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Find the first occurrence of an integer in the given sorted sequence of integers (possibly with duplicates).

# O(log n)
def binary_search_with_duplicates(a, low, high, key):
    if high < low:
        return -1
    mid = (low + high) // 2
    if key == a[mid] and (mid == 0 or key != a[mid - 1]):
        return mid
    elif key > a[mid]:
        return binary_search_with_duplicates(a, mid + 1, high, key)
    else:
        return binary_search_with_duplicates(a, low, mid - 1, key)

# O(log n)
def binary_search_with_duplicates_iterative(a, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if key == a[mid] and (mid == 0 or key != a[mid - 1]):
            return mid
        elif key > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))

    for x in b:
        index = binary_search_with_duplicates(a, 0, n - 1, x)
        print(index, end=' ')