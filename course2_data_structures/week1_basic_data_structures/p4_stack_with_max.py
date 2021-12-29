# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Implement a stack supporting the operations Push(), Pop(), and Max() in constant time.

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def Push(self, a):
        if len(self.__max_stack):
            self.__max_stack.append(max(a, self.__max_stack[-1]))
        else:
            self.__max_stack.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        elem = self.__stack.pop()
        if self.__max_stack[-1] == elem:
            self.__max_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
