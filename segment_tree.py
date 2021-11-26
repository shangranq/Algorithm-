class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.total = 0
        self.left = None
        self.right = None
        
class SegTree:
    def __init__(self, nums):
      
        def _build(nums, l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node
            mid = (l + r) // 2
            node = Node(l, r)
            node.left = _build(nums, l, mid)
            node.right = _build(nums, mid+1, r)
            node.total = node.left.total + node.right.total
            return node
        
        self.root = _build(nums, 0, len(nums)-1)

    def update(self, i, val):
        
        def _update(node, i, val):
            if node.s == node.e:
                node.total += val
                return node
            mid = (node.s + node.e) // 2
            if mid >= i:
                node.left = _update(node.left, i, val)
            else:
                node.right = _update(node.right, i, val)
            node.total = node.left.total + node.right.total
            return node
          
        self.root = _update(self.root, i, val)
        
    def range(self, l, r):
      
        def _range(node, l, r):
            if l <= node.s and node.e <= r:
                return node.total
            if l > node.e or r < node.s:
                return 0
            return _range(node.left, l, r) + _range(node.right, l, r)
          
        return _range(self.root, l, r)
      
