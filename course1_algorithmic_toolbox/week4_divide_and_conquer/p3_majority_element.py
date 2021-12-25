# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to check whether an input sequence contains a majority element.

# O(n^2)
def get_majority_element_naive(a):
    for i in range(0, len(a)):
        current = a[i]
        count = 0
        for j in range(0, len(a)):
            if a[j] == current:
                count += 1
        if count > len(a) / 2:
            return 1
    return 0

# O(n log n)
def merge_sort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])
    return merge(l, r)

# O(n)
def merge(l, r):
    i = j = k = 0
    arr = [None] * (len(l) + len(r))
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

    return arr

# O(n)
def count_sort(a):
    count = {}
    for i in range(0, len(a)):
        if a[i] in count:
            count[a[i]] += 1
        else:
            count[a[i]] = 1
    return count

# O(n)
def moore_voting_algorithm(a):
    candidate, count = a[0], 1
    for i in range(1, len(a)):
        if count == 0:
            candidate = a[i]
        if a[i] == candidate:
            count += 1
        else:
            count -= 1
    return candidate

# O(n)
def is_majority(a, candidate):
    count = 0
    for i in range(len(a)):
        if a[i] == candidate:
            count += 1
    
    if count > len(a) // 2:
        return True
    else:
        return False

# O(n log n)
def get_majority_element_imp1(a):
    sorted = merge_sort(a)
    count, temp, max_count = 1, sorted[0], 1
    for i in range(1, len(sorted)):
        if temp == sorted[i]:
            count += 1
        else:
            count = 1
            temp = sorted[i]
        if count > max_count:
            max_count = count
            if max_count > len(sorted) // 2:
                return 1
    return 0

# O(n)
def get_majority_element_imp2(a):
    sorted = count_sort(a)
    
    for key in sorted:
        if sorted[key] > len(sorted) // 2:
            return 1
    return 0

# O(n)
def get_majority_element_imp3(a):
    candidate = moore_voting_algorithm(a)
    if is_majority(a, candidate):
        return 1
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
     
    print(get_majority_element_imp3(a))