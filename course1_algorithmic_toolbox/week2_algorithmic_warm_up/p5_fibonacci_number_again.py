# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).

def calc_fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

def calc_huge_fib_mod_naive(n, m):
    fib = calc_fib(n)
    return fib % m

def calc_pisano_period(m):
    previous, current = 0, 1
    for i in range (0, m * m):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1

def calc_huge_fib_mod(n, m):
    pisano_period = calc_pisano_period(m)
    remainder = n % pisano_period
    return calc_fib(remainder) % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(calc_huge_fib_mod(n, m))