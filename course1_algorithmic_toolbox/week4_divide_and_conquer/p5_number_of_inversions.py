# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this problem is to count the number of inversions of a given sequence.

# O(n^2)
def num_of_inversions_naive(a):
    inversions = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] > a[j]):
                inversions += 1
 
    return inversions

# O(n log n)
def merge_sort(a, b, left, right):
    inversions = 0
    
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort(a, b, left, mid)
        inversions += merge_sort(a, b, mid + 1, right)
        inversions += merge(a, b, left, mid, right)
        
    return inversions

# O(n)
def merge(a, b, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv = 0

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            inv += (mid - i + 1)
            j += 1

        k += 1

    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1

    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    
    for h in range(left, right + 1):
        a[h] = b[h]

    return inv

# O(n log n)
def num_of_inversions(a):
    return merge_sort(a, [None] * len(a), 0, len(a) - 1)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
     
    print(num_of_inversions(a))
