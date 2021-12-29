# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to find errors in the usage of brackets in a string.

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

# O(1)
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

# O(n)
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        elif next in ")]}":
            bracket = opening_brackets_stack.pop()
            if not are_matching(bracket.char, next):
                return i + 1
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[0].position + 1

if __name__ == "__main__":
    text = input()
    print(find_mismatch(text))
    


