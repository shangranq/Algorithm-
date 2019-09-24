"""
binary search for an element from an array; return index of the element if exists, otherwise return -1
"""
def binary_find(A, a):
    def helper(A, a, low, high):
        if low > high: return -1
        mid = (low + high) // 2
        if A[mid] == a:
            return mid
        if A[mid] > a:
            return helper(A, a, low, mid-1)
        return helper(A, a, mid+1, high)
    return helper(A, a, 0, len(A)-1)

"""
binary insort an element into an array; return index where this element is supposed to be. 
If there is a same element found, put on the right of this element.
"""
def binary_insert_right(A, a):
    def helper(A, a, low, high):
        if low == high:
            return low if A[low] > a else low + 1
        mid = (low + high) // 2
        if A[mid] == a:
            return mid + 1
        if A[mid] > a:
            return helper(A, a, low, mid-1)
        return helper(A, a, mid+1, high)
    return helper(A, a, 0, len(A)-1)

"""
binary insort an element into an array; return index where this element is supposed to be. 
If there is a same element found, put on the left of this element.
"""
def binary_insert_left(A, a):
    def helper(A, a, low, high):
        if low == high:
            return low if A[low] >= a else low + 1
        mid = (low + high) // 2
        if A[mid] == a:
            return mid
        if A[mid] > a:
            return helper(A, a, low, mid-1)
        return helper(A, a, mid+1, high)
    return helper(A, a, 0, len(A)-1)

x = [1,2,3,4,5,6,7,8,9]
print(binary_insert_left(x, 5))
print(binary_insert_right(x, 5))
