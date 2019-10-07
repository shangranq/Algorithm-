def heapify(array, i, n):
    # heapify the ith node among the first n elements of array
    smallest = i
    l, r = 2*i+1, 2*i+2
    if l < n and array[l]  < array[smallest]:
        smallest = l
    if r < n and array[r] < array[smallest]:
        smallest = r
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, smallest, n)

def build_min_heap(A):
    for i in range(len(A)//2, -1, -1):
        heapify(A, i, len(A))
