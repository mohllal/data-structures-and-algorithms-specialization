# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given a set of 𝑛 segments {[𝑎0,𝑏0],[𝑎1,𝑏1],...,[𝑎𝑛−1,𝑏𝑛−1]} with integer coordinates on a line, find the minimum number 𝑚 of points such that each segment contains at least one point. 
# That is, find a set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖,𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.

def optimal_points(segments):
    points = []
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        ipt = input()
        segments.append(list(map(int, ipt.split())))
    segments.sort()
    res = optimal_points(segments)
    print(len(res))
    for x in res:
        print(x, end=' ')