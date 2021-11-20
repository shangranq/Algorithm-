class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.count = 1 # count is used for augment the non-unique elements
        self.height = 1 # height is for maintaining the balanced property of AVL tree
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        
        def _insert(root, key):
            if root is None:
                return Node(key)
            else:
                if root.val == key:
                    root.count += 1
                    return root
                elif root.val < key:
                    root.right = _insert(root.right, key)
                else:
                    root.left = _insert(root.left, key)
                
                root.height = self.updateHeight(root)
                balance = self.getBalance(root)

                if balance > 1 and self.getBalance(root.left) > 0:
                    return self.rightRotate(root)

                if balance < -1 and self.getBalance(root.right) < 0:
                    return self.leftRotate(root)

                if balance > 1 and self.getBalance(root.left) < 0:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)

                if balance < -1 and self.getBalance(root.right) > 0:
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)
                
            return root
        
        self.root = _insert(self.root, key)
        
    def delete(self, key):
        
        def _delete(root, key):
            if root is None:
                return root
            if key < root.val:
                root.left = _delete(root.left, key)
            elif key > root.val:
                root.right = _delete(root.right, key)
            else:
                root.count -= 1
                if root.count > 0:
                    return root
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    nxt = root.right
                    while nxt and nxt.left:
                        nxt = nxt.left
                    root.val = nxt.val
                    root.count = nxt.count
                    nxt.count = 0
                    root.right = _delete(root.right, nxt.val)
                    
                root.height = self.updateHeight(root)
                balance = self.getBalance(root)

                if balance > 1 and self.getBalance(root.left) > 0:
                    return self.rightRotate(root)

                if balance < -1 and self.getBalance(root.right) < 0:
                    return self.leftRotate(root)

                if balance > 1 and self.getBalance(root.left) < 0:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)

                if balance < -1 and self.getBalance(root.right) > 0:
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)
                    
            return root
        
        self.root = _delete(self.root, key)
        
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
    
# example solution of the LC 218
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        OPEN, END = 1, 0
        ans = []
        pool = []
        xs = set()
        for l, r, h in buildings:
            pool.append([l, OPEN, h])
            pool.append([r, END, h])
            xs.add(l)
            xs.add(r)
        pool.sort()
        xs = sorted(list(xs))
        
        bst = AVLTree()
        p_idx = 0
        for x in xs:
            while p_idx < len(pool) and pool[p_idx][0] == x:
                _, status, h = pool[p_idx]
                if status == OPEN:
                    bst.insert(h)
                else:
                    bst.delete(h)
                p_idx += 1
            max_height = bst.findMax()
            if ans and ans[-1][1] == max_height:
                continue
            ans.append([x, max_height])
        return ans
    
