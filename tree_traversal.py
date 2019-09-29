# inorder
def inorder(root):
    node = root
    stack = []
    while True:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node.val)
            node = node.right
        else:
            break

def inorder1(root):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.value)
        node = node.right

def inorder2(root):
    stack = [root]
    while stack[-1].left:
        stack.append(stack[-1].left)
    while stack or node:
        node = stack.pop()
        node = node.right
        while node:
            stack.append(node)
            node = node.left
        print(node.value)
        node = node.right

# preorder, root, left, right
def preorder(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# postorder, left, right, root
def postorder(root):
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while ans:
        node = node.pop()
        print(node.val)
