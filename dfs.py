def DFS(i, visited, adj, ans):
    visited[i] = 1           # Mark the current node as visited
    ans.append(i)            # Add it to the traversal result
    for neighbor in adj[i]:  # Traverse its neighbors
        if visited[neighbor] == 0:
            DFS(neighbor, visited, adj, ans)  # Recursive DFS call

def dfs(adj):
    v = len(adj)             # Number of vertices
    visited = [0] * v        # Visited list
    ans = []                 # Result list
    for i in range(v):       # Loop through all nodes
        if visited[i] == 0:  # If node is not visited
            DFS(i, visited, adj, ans)  # Start DFS from node i
    return ans

# Example usage
adj = [
    [1, 2],  # Node 0
    [0, 3],  # Node 1
    [0],     # Node 2
    [1],     # Node 3
    []       # Node 4 (disconnected)
]

print(dfs(adj))  # Output: [0, 1, 3, 2, 4]
