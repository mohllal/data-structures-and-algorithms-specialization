# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to design an algorithm that is able to preprocess a given string 𝑠 to answer any query of the form “are these two substrings of 𝑠 equal?” efficiently

class Solver:
	def __init__(self, s):
		self.s = s
	def ask(self, a, b, l):
		return s[a:a+l] == s[b:b+l]

if __name__ == '__main__':
    s = input()
    q = int(input())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, input().split())
        print("Yes" if solver.ask(a, b, l) else "No")
