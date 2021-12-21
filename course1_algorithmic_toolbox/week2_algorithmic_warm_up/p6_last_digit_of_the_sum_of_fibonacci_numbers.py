# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given an integer 𝑛, find the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛.

# O(n)
def calc_fib_sum_naive(n):
    current, next, sum = 0, 1, 0
    for i in range(0, n):
        next, current = next + current, next
        sum += current

    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(calc_fib_sum_naive(n))