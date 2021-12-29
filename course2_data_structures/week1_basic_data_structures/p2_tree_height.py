# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to compute and output the height of a rooted tree.

class Node:
    def __init__(self, key):
        self.key = key
        self.child = []

# O(n^2)
def compute_height_naive(n, parents):
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

# O(n)
def build_tree(n, parents):
    nodes = [Node(i) for i in range(n)]
    for i in range(n):
        if parents[i] != -1:
            nodes[parents[i]].child.append(nodes[i])
    return nodes[0]

# O(n)
def bfs_iterative(root):
    if root == None:
        return 0
    
    queue = [root]
    height = 0
    
    while len(queue) != 0:
        height += 1
        for i in range(len(queue)):
            node = queue.pop(0)
            for child in node.child:
                queue.append(child)

    return height

# O(n)
def compute_height(n, parents):
    root = build_tree(n, parents)
    return bfs_iterative(root)

if __name__ == "__main__":
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_naive(n, parents))