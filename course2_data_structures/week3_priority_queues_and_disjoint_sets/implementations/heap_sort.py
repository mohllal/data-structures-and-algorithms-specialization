# In-Place Heap Sort

# O(n log n) time and O(1) space
def build_heap(arr, n):
    for i in range(n // 2, -1, -1):
        sift_down(arr, n, i)

# O(log n) time and O(1) space
def sift_down(arr, n, i):
    # recursive sift down until the root is reached or the child is larger
    largest = i
        
    l = (2 * i) + 1
    if l < n and arr[largest] < arr[l]:
        largest = l
    
    r = (2 * i) + 2
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, n, largest)

# O(n log n) time and O(1) space
def heap_sort(arr):
    # 1. build heap in place
    # 2. for n - 1 times
    # 2.1 swap the last element with the root
    # 2.2 sift down the root
    n = len(arr)
    build_heap(arr, n)

    size = n - 1
    for _ in range(1, n):
        arr[0], arr[size] = arr[size], arr[0]
        size = size - 1
        sift_down(arr, size, 0)
        
if __name__ == '__main__':
   arr = [1, 4, 3, 5, 6, 0, 2, 7]
   
   heap_sort(arr)
   print(arr)
    