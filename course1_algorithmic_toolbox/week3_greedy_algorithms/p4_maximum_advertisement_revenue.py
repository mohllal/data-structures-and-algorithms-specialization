# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot). 
# We need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗) such that the sum of their products is maximized.

# O(n log n)
def max_dot_product(a, b):
    res = 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(len(a)):
        res += (a[i] * b[i])
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b))
    

