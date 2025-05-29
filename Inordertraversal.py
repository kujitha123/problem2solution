class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = [root]
    i = 1
    while q and i < len(nodes):
        current = q.pop(0)
        if nodes[i] != -1:
            current.left = TreeNode(nodes[i])
            q.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] != -1:
            current.right = TreeNode(nodes[i])
            q.append(current.right)
        i += 1
    return root

from collections import defaultdict

def inorder_by_level(root):
    levels = defaultdict(list)
    def dfs(node, depth):
        if not node:
            return
        dfs(node.left, depth + 1)
        levels[depth].append(node.val)
        dfs(node.right, depth + 1)
    dfs(root, 0)
    return [levels[d] for d in sorted(levels)]

n = list(map(int, input().split()))
root = build_tree(n)
print(inorder_by_level(root))
