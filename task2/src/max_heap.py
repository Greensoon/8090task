# max heap
import random

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # heapify up
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    # insert element
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, i, size):
        max_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < size and self.heap[left] > self.heap[max_idx]:
            max_idx = left

        if right < size and self.heap[right] > self.heap[max_idx]:
            max_idx = right

        if max_idx != i:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self.heapify_down(max_idx, size)

    # heap sort
    def heap_sort(self):
        n = len(self.heap)
        
        # build heap from array
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i, n)

        # extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify_down(0, i)

        return self.heap

# test max heap 
if __name__ == "__main__":
    # arr = []
    # arr = [5]
    # arr = [1,2,3,4,5]
    # arr = [5,4,3,2,1]
    # arr = [3,1,4,1,5,9]
    # arr = [9, 4, 2, 7, 5, 1, 93, 28, 116]
    
    arr = random.sample(range(100000), 10000)
    heap = MaxHeap()
    for num in arr:
        heap.insert(num)
    sorted_arr = heap.heap_sort()
    print("Original array:", arr)
    print("Heap sort result:", sorted_arr)
    print()
