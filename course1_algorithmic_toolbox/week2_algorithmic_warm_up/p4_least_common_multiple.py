# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given two integers 𝑎 and 𝑏, find their least common multiple.

def calc_lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a * b

def calc_gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return calc_gcd(b, r)

def calc_lcm(a, b):
    gcd = calc_gcd(a, b)
    return (a * b) // gcd

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(calc_lcm(a, b))
