class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes or nodes[0] == -1:
        return None
    root = TreeNode(nodes[0])
    q = [(root, 0)]  # node with its depth
    i = 1
    while q and i < len(nodes):
        current, depth = q.pop(0)
        if i < len(nodes) and nodes[i] != -1:
            current.left = TreeNode(nodes[i])
            q.append((current.left, depth + 1))
        i += 1
        if i < len(nodes) and nodes[i] != -1:
            current.right = TreeNode(nodes[i])
            q.append((current.right, depth + 1))
        i += 1
    return root

from collections import defaultdict

def get_node_levels(root):
    node_levels = {}
    def assign_levels(node, level):
        if not node:
            return
        node_levels[node] = level
        assign_levels(node.left, level + 1)
        assign_levels(node.right, level + 1)
    assign_levels(root, 0)
    return node_levels

def inorder_by_level(root):
    node_levels = get_node_levels(root)
    levels = defaultdict(list)
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        levels[node_levels[node]].append(node.val)
        inorder(node.right)
    inorder(root)
    return [levels[d] for d in sorted(levels)]

# --- Input and Execution ---
n = list(map(int, input().split()))
root = build_tree(n)
print(inorder_by_level(root))
