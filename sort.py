from heap import heapify, build_min_heap

A = [1,4,5,6,34,2,50,8,4,3,7,7,5]

def quicksort(A, low, high):
    if low >= high: return
    pivot = (low + high) // 2
    a =  A[pivot]
    A[pivot], A[high] = A[high], A[pivot]
    sorted_count = low
    for i in range(low, high):
        if A[i] <= a:
            A[sorted_count], A[i] = A[i], A[sorted_count]
            sorted_count += 1
    A[sorted_count], A[high] = A[high], A[sorted_count]
    quicksort(A, low, sorted_count-1)
    quicksort(A, sorted_count+1, high)
    
def heapsort(A):
    build_min_heap(A)
    A[0], A[-1] = A[-1], A[0]
    for i in range(len(A)-2, -1, -1):
        heapify(A, 0, i+1)
        A[i], A[0] = A[0], A[i]

quicksort(A, 0, len(A)-1)
print(A)
