# Disjoint Set (Union by rank & Path compression)

class DisjointSet:
    def __init__(self):
        pass
    
    # O(n) time and O(n) space
    def create(self, n):
        # create `n` disjoint sets (one for each item)
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    # O(log n) time and O(1) space
    def find(self, x):
        # if `x` is not the root of the set
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # O(log n) time and O(1) space
    def union(self, a, b):
        # find the root of the sets in which elements `x` and `y` belongs
        x = self.find(a)
        y = self.find(b)
 
        # if `x` and `y` are present in the same set
        if x == y:
            return
 
        # union by rank: attach the smaller depth tree under the root of the deeper tree.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] = self.rank[y] + 1
    
    def print(self):
        print('parent:', self.parent)
        print('rank:', self.rank)
        print ('\n')

if __name__ == '__main__':
    n = 5
 
    # initialize `DisjointSet` class
    ds = DisjointSet()
 
    # create a singleton set for each element of the universe
    ds.create(n)
    ds.print()
 
    ds.union(4, 3)        # 4 and 3 are in the same set
    ds.print()
 
    ds.union(2, 1)        # 1 and 2 are in the same set
    ds.print()
 
    ds.union(1, 3)        # 1, 2, 3, 4 are in the same set
    ds.print()
    
    