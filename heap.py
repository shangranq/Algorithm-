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

        
        
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.table = {}
        self.len = 0

    def heapify(self, idx):
        pareIdx = (idx - 1) // 2
        if pareIdx >= 0 and self.heap[pareIdx] < self.heap[idx]:
            self.heap[pareIdx], self.heap[idx] = self.heap[idx], self.heap[pareIdx]
            self.table[self.heap[pareIdx]] = pareIdx
            self.table[self.heap[idx]] = idx
            self.heapify(pareIdx)
            return
        left, right = idx * 2 + 1, idx * 2 + 2
        if right >= self.len:
            if left < self.len and self.heap[idx] < self.heap[left]:
                self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                self.table[self.heap[left]] = left
                self.table[self.heap[idx]] = idx
                self.heapify(left)
        else:
            if max(self.heap[left], self.heap[right]) > self.heap[idx]:
                if self.heap[left] >= self.heap[right]:
                    self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                    self.table[self.heap[left]] = left
                    self.table[self.heap[idx]] = idx
                    self.heapify(left)
                else:
                    self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                    self.table[self.heap[right]] = right
                    self.table[self.heap[idx]] = idx
                    self.heapify(right)

    def heappush(self, val):
        self.heap.append(val)
        self.table[val] = self.len
        self.len += 1
        self.heapify(self.len-1)

    def heappop(self):
        val = self.heap[0]
        self.len -= 1
        del self.table[val]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.table[self.heap[0]] = 0
        self.heapify(0)

    def heapRemove(self, val):
        idx = self.table[val]
        del self.table[val]
        self.len -= 1
        if idx == self.len:
            self.heap.pop()
            return
        self.heap[idx] = self.heap[-1]
        self.table[self.heap[idx]] = idx
        self.heap.pop()
        self.heapify(idx)

    def heapUpdate(self, old_val, new_val):
        idx = self.table[old_val]
        del self.table[old_val]
        self.heap[idx] = new_val
        self.table[new_val] = idx
        self.heapify(idx)

heap = MaxHeap()
for a in [2,3,4,5,6,7]:
    heap.heappush(a)
print(heap.heap, heap.table)
heap.heapUpdate(7, -1)
print(heap.heap, heap.table)
heap.heapRemove(4)
print(heap.heap, heap.table)
