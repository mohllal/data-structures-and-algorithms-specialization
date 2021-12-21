# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# You are going to travel to another city that is located 𝑑 miles away from your home city. 
# Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. 
# Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city. 
# What is the minimum number of refills needed?

# O(n)
def compute_min_refills(m, n, stops):
    num_refills = 0
    current_refill = 0
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and stops[current_refill + 1] - stops[last_refill] <= m:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [0] + list(map(int, input().split())) + [d]
    print(compute_min_refills(m, n, stops))