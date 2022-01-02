# Binary Min Heap

class BinaryMinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        # parent of i = (i - 1) / 2
        return (i - 1) // 2
    
    def left(self, i):
        # left child of i = 2 * i + 1
        return (2 * i) + 1
    
    def right(self, i):
        # right child of i = 2 * i + 2
        return (2 * i) + 2

    # O(1) time and O(1) space
    def get_max(self):
        return self.heap[0]
    
    # O(log n) time and O(1) space
    def extract_max(self):
        # 1. swap the last element with the root
        # 2. remove the last element
        # 3. sift down the root
        max = self.heap[0]

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.sift_down(0)
        return max
    
    # O(log n) time and O(1) space
    def insert(self, x):
        # 1. insert the new element at the end
        # 2. sift up the new element
        self.heap.append(x)
        size = len(self.heap)
        self.sift_up(size - 1)
    
    # O(log n) time and O(1) space
    def sift_up(self, i):
        # recursive sift up until the root is reached or the parent is smaller
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    # O(log n) time and O(1) space
    def sift_down(self, i):
        # recursive sift down until the root is reached or the child is smaller
        smallest = i
        size = len(self.heap)
        
        l = self.left(i)
        if l < size and self.heap[smallest] > self.heap[l]:
            smallest = l
        
        r = self.right(i)
        if r < size and self.heap[smallest] > self.heap[r]:
            smallest = r
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.sift_down(smallest)

    
    # O(log n) time and O(1) space
    def delete(self, i):
        # 1. change priority of the element to be deleted to -infinity
        # 2. sift up the element to the root
        # 3. extract the root
        self.heap[i] = float('-inf')
        
        self.sift_up(i)
        self.extract_max()
    
    # O(log n) time and O(1) space
    def change_value(self, i, x):
        # 1. change the value of the element to x
        # 2. sift up or down based on the new value
        old = self.heap[i]
        self.heap[i] = x
        
        if x < old:
            self.sift_up(i)
        else:
            self.sift_down(i)
    
    def print(self):
        print('heap:', self.heap)

if __name__ == '__main__':
    # initialize `BinaryMinHeap` class
    minh = BinaryMinHeap()
 
    # push elements into the heap
    minh.insert(3)
    minh.insert(2)
    minh.insert(1)
    minh.insert(5)
    minh.insert(6)
    minh.insert(7)
    minh.insert(0)
    minh.insert(8)
    minh.print() # heap: [0, 3, 1, 5, 6, 7, 2, 8]
    
    minh.extract_max()
    minh.print() # heap: [1, 3, 2, 5, 6, 7, 8]
    
    minh.delete(2)
    minh.print() # heap: [1, 3, 7, 5, 6, 8]
    
    minh.delete(1)
    minh.print() # heap: [1, 5, 7, 8, 6]
    
    minh.change_value(0, 20)
    minh.print() # heap: [5, 6, 7, 8, 20]
    
    minh.change_value(4, -10)
    minh.print() # heap: [-10, 5, 7, 8, 6]
    
    
    