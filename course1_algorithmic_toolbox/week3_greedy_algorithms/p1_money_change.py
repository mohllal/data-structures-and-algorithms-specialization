# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

# O(n)
def get_change(m):
    count = 0
    while m > 0:
        if m >= 10:
            m -= 10
        elif m >= 5:
            m -= 5
        elif m >= 1:
            m -= 1
        count += 1 
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))