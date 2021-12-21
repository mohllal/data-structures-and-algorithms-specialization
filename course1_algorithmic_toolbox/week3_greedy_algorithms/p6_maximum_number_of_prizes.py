# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise distinct positive integers as possible. 
# That is, to find the maximum 𝑘 such that 𝑛 can be written as 𝑎1 + 𝑎2 +···+ 𝑎𝑘 where 𝑎1,...,𝑎𝑘 are positive integers and 𝑎𝑖 != 𝑎𝑗 for all 1 ≤𝑖 < 𝑗 ≤ 𝑘.

# O(n)
def optimal_sum(n):
    res = []
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if sum <= n:
            res.append(i)
        else:
            remain = n - (sum - i)
            res[-1] += remain
            break
    return res

if __name__ == '__main__':
    n = int(input())
    res = optimal_sum(n)
    print(len(res))
    for x in res:
        print(x, end=' ')
