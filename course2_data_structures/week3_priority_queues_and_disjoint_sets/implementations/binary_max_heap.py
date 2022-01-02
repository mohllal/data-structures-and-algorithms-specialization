# Binary Max Heap

class BinaryMaxHeap:
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
        # recursive sift up until the root is reached or the parent is larger
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    # O(log n) time and O(1) space
    def sift_down(self, i):
        # recursive sift down until the root is reached or the child is larger
        largest = i
        size = len(self.heap)
        
        l = self.left(i)
        if l < size and self.heap[largest] < self.heap[l]:
            largest = l
        
        r = self.right(i)
        if r < size and self.heap[largest] < self.heap[r]:
            largest = r
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.sift_down(largest)

    
    # O(log n) time and O(1) space
    def delete(self, i):
        # 1. change priority of the element to be deleted to +infinity
        # 2. sift up the element to the root
        # 3. extract the root
        self.heap[i] = float('inf')
        
        self.sift_up(i)
        self.extract_max()
    
    # O(log n) time and O(1) space
    def change_value(self, i, x):
        # 1. change the value of the element to x
        # 2. sift up or down based on the new value
        old = self.heap[i]
        self.heap[i] = x
        
        if x > old:
            self.sift_up(i)
        else:
            self.sift_down(i)
    
    def print(self):
        print('heap:', self.heap)

if __name__ == '__main__':
    # initialize `BinaryMaxHeap` class
    maxh = BinaryMaxHeap()
 
    # push elements into the heap
    maxh.insert(3)
    maxh.insert(2)
    maxh.insert(1)
    maxh.insert(5)
    maxh.insert(6)
    maxh.insert(7)
    maxh.insert(0)
    maxh.insert(8)
    maxh.print() # heap: [8, 7, 6, 5, 3, 1, 0, 2]
    
    maxh.extract_max()
    maxh.print() # heap: [7, 5, 6, 2, 3, 1, 0]
    
    maxh.delete(2)
    maxh.print() # heap: [7, 5, 1, 2, 3, 0]
    
    maxh.delete(1)
    maxh.print() # heap: [7, 3, 1, 2, 0]
    
    maxh.change_value(0, -1)
    maxh.print() # heap: [3, 2, 1, -1, 0]
    
    maxh.change_value(4, 10)
    maxh.print() # heap: [3, 2, 1, -1, 0]
    
    
    