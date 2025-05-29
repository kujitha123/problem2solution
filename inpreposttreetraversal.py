class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
    
def preorder(root):
    if(root==None):
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Inorder traversal:")
inorder(root)
print("\nPreorder traversal:")
preorder(root)
print("\nPostorder traversal:")
postorder(root)