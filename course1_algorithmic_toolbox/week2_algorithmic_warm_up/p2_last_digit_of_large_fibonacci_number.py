# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given an integer n, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).

# O(n)
def calc_last_digit_of_large_fib_number_naive(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n] % 10

# O(n)
def calc_last_digit_of_large_fib_number(n):
    f = [0, 1]
    for i in range(2, n + 1):
        current = (f[i - 1] + f[i - 2]) % 10
        f.append(current)
    return f[n]


if __name__ == '__main__':
    n = int(input())
    print(calc_last_digit_of_large_fib_number(n))

