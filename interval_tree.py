class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
        self.height = 1
        
class IntervalTree:
    def __init__(self):
        self.root = None
        
    def insert(self, start, end):
             
        def _insert(root, start, end):
            if root is None:
                return Node(start, end), True
            succeed = False
            if root.e <= start:
                root.right, succeed = _insert(root.right, start, end)
            elif root.s >= end:
                root.left, succeed = _insert(root.left, start, end)
            else: # overlap happened between root and new node[start, end]
                return root, False
            if succeed:
                root.height = self.updateHeight(root)
                root = self.rebalance(root)
            return root, succeed
        
        self.root, status = _insert(self.root, start, end)
        return status
        
    def delete(self, start, end):
      
        def _delete(root, start, end):
            if not root:
                return root
            if root.e <= start:
                root.right = _delete(root.right, start, end)
            elif root.s >= end:
                root.left = _delete(root.left, start, end)
            else:
                # need to remove the root itself
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                nxt = root.right
                while nxt and nxt.left: 
                    nxt = nxt.left
                root.s, root.e = nxt.s, nxt.e
                root.right = _delete(root.right, nxt.s, nxt.e)
            root.height = self.updateHeight(root)
            root = self.rebalance(root)
            return root
          
        self.root = _delete(self.root, start, end)
        
    def rebalance(self, node):
        balance = self.getBalance(node)

        if balance > 1 and self.getBalance(node.left) > 0:
            return self.rightRotate(node)

        if balance < -1 and self.getBalance(node.right) < 0:
            return self.leftRotate(node)

        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
        
    def findMax(self):
        if self.root == None:
            return 0
        node = self.root
        while node and node.right:
            node = node.right
        return node.val
    
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = self.updateHeight(z)
        y.height = self.updateHeight(y)
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = self.updateHeight(z)
        y.height = self.updateHeight(y)
 
        # Return the new root
        return y
    
    def updateHeight(self, node):
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
 
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
        
# example usage of IntervalTree in LC 391      
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        area = 0
        pool = []
        min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')
        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)
            pool.append([x, 1, y, b])
            pool.append([a, 0, y, b])
            min_x = min(min_x, x)
            max_x = max(max_x, a)
            min_y = min(min_y, y)
            max_y = max(max_y, b)
            
        if area != ((max_x - min_x) * (max_y - min_y)):
            return False
        
        pool.sort()
        tree = IntervalTree()
        
        for x, status, y1, y2 in pool:
            if status == 0:
                tree.delete(y1, y2)
            else:
                if not tree.insert(y1, y2):
                    return False
        return True
            
