# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to convert a given array of integers into a heap by applying a certain number of swaps to the array.

# O(n^2) time and O(n) space
def num_of_swaps_naive(data):
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

# O(n log n) time and O(1) space
def build_heap(arr, n):
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(arr, n, i, swaps)
        
    return swaps

# O(log n) time and O(1) space
def sift_down(arr, n, i, swaps):
    # recursive sift down until the root is reached or the child is smaller     
    smallest = i
        
    l = (2 * i) + 1
    if l < n and arr[smallest] > arr[l]:
        smallest = l
    
    r = (2 * i) + 2
    if r < n and arr[smallest] > arr[r]:
        smallest = r
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))
        sift_down(arr, n, smallest, swaps)

def num_of_swaps(arr):
    return build_heap(arr, len(arr))

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = num_of_swaps(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
