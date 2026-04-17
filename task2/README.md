# Heap Sort

## 1. Heap
### 1.1 Abstract Data Type (ADT) Definition

A heap is a specialized tree-based data structure that satisfies the heap property:
- For a max heap, the value of each parent node is greater than or equal to the values of its children
- For a min heap, the value of each parent node is less than or equal to the values of its children

#### Operations
- **insert(value)**: Add a new element to the heap while maintaining the heap property
- **heapify_up(i)**: Move an element up the heap to maintain the heap property
- **heapify_down(i, size)**: Move an element down the heap to maintain the heap property
- **heap_sort()**: Sort an array using the heap data structure

## 2. Implementation

### 2.1 Max Heap Implementation

The `MaxHeap` class in `src/max_heap.py` implements a max heap with the following features:

- **parent(i)**: Returns the index of the parent node
- **left_child(i)**: Returns the index of the left child
- **right_child(i)**: Returns the index of the right child
- **heapify_up(i)**: Maintains the heap property by moving an element up
- **insert(value)**: Adds a new element to the heap
- **heapify_down(i, size)**: Maintains the heap property by moving an element down
- **heap_sort()**: Sorts the heap in ascending order

### 2.2 Heap Sort Algorithm

The heap sort algorithm consists of two main phases:
1. **Build Max Heap**: Convert the input array into a max heap
2. **Extract Elements**: Repeatedly extract the maximum element and heapify the remaining elements

## 3. Time Complexity Analysis

### 3.1 Insert Operation
- **Time Complexity**: O(log n)
- **Explanation**: Each insertion may require moving the element up the heap, which takes at most log n steps

### 3.2 Heapify Operations
- **heapify_up**: O(log n)
- **heapify_down**: O(log n)

### 3.3 Heap Sort
- **Time Complexity**: O(n log n)
- **Explanation**:
  - Building the heap: O(n)
  - Extracting elements: O(n log n)
  - Overall: O(n log n)

## 4. Space Complexity

- **Space Complexity**: O(1) auxiliary space
- **Explanation**: Heap sort is an in-place sorting algorithm, meaning it doesn't require additional storage proportional to the input size

## 5. Example Usage

```python
from src.max_heap import MaxHeap

# Create a max heap
heap = MaxHeap()

# Insert elements
arr = [9, 4, 2, 7, 5, 1, 93, 28, 116]
for num in arr:
    heap.insert(num)

# Sort the array
sorted_arr = heap.heap_sort()
print("Original array:", arr)
print("Heap sort result:", sorted_arr)
```

## 6. Test Results

```
Original array: [9, 4, 2, 7, 5, 1, 93, 28, 116]
Heap sort result: [1, 2, 4, 5, 7, 9, 28, 93, 116]
```

## 7. Advantages of Heap Sort

- **Efficiency**: O(n log n) time complexity for all cases
- **In-place**: Requires no additional memory
- **Guaranteed performance**: Unlike quicksort, heap sort has a consistent O(n log n) time complexity
- **Useful for priority queues**: The heap data structure is the basis for priority queue implementations

## 8. Applications

- **Sorting large datasets**
- **Priority queues**
- **Graph algorithms** (e.g., Dijkstra's algorithm)
- **Selection algorithms** (e.g., finding the k-th largest element)
