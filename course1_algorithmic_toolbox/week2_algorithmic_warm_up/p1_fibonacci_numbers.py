# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.

# O(2^n)
def calc_fib_naive(n):
    if (n <= 1):
        return n
    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

# O(n)
def calc_fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))

