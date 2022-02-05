# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to find all text locations where distance from pattern is sufficiently small.
import sys

def solve(k, text, pattern):
	return []

if __name__ == '__main__':
    for line in sys.stdin.readlines():
        k, t, p = line.split()
        ans = solve(int(k), t, p)
        print(len(ans), *ans)
