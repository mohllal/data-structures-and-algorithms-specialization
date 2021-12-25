# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to implement the binary search algorithm.

# O(log n)
def binary_search(a, low, high, key):
    if high < low:
        return -1
    mid = (low + high) // 2
    if key < a[mid]:
        return binary_search(a, low, mid - 1, key)
    elif key > a[mid]:
        return binary_search(a, mid + 1, high, key)
    else:
        return mid

# O(log n)
def binary_search_iterative(a, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if key < a[mid]:
            high = mid - 1
        elif key > a[mid]:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))

    for x in b:
        index = binary_search(a, 0, n - 1, x)
        print(index, end=' ')