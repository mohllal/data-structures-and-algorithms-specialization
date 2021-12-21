# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Compute the last digit of 𝐹0^2 +𝐹1^2 +···+𝐹𝑛^2.

# O(n)
def calc_fib_square_sum_naive(n):
    current, next, sum = 0, 1, 0
    for i in range(0, n):
        next, current = next + current, next
        sum += current ** 2

    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(calc_fib_square_sum_naive(n))