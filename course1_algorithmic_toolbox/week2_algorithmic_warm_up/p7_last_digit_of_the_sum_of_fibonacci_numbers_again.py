# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + ···+𝐹𝑛.

# O(n)
def calc_fib_partial_sum_naive(m, n):
    current, next, sum = 0, 1, 0
    for i in range(0, n + 1):
        if i >= m:
            sum += current
        next, current = next + current, next

    return sum % 10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(calc_fib_partial_sum_naive(m, n))