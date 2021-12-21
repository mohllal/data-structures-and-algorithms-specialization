# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given two integers 𝑎 and 𝑏, find their greatest common divisor.

def calc_gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd

def calc_gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return calc_gcd(b, r)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(calc_gcd(a, b))

