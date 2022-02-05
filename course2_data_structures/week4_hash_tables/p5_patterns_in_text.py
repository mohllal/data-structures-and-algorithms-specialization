# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is given two strings 𝑠 and 𝑡 and the goal is to find a string 𝑤 of maximal length that is a substring of both 𝑠 and 𝑡.

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

if __name__ == '__main__':
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve(s, t)
        print(ans.i, ans.j, ans.len)
