# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Compose the largest number out of a set of integers.

def is_greater_or_equal(a, b):
    a_str = str(a)
    b_str = str(b)
    return int(a_str + b_str) >= int(b_str + a_str)

# O(n)
def largest_number(a):
    res = ""
    while len(a) > 0:
        max = 0
        for digit in a:
            if is_greater_or_equal(digit, max):
                max = digit
        res += str(max)
        a.remove(max)
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(largest_number(a))