def BFS(q, visited, adj, ans):
    while q:
        node = q.pop(0)
        ans.append(node)
        for it in adj[node]:
            if not visited[it]:
                visited[it] = 1
                q.append(it)
def bfs(adj):
    v = len(adj)
    visited = [0] * v
    ans = []
    for i in range(v):
        if not visited[i]:
            visited[i] = 1
            q = [i]
            BFS(q, visited, adj, ans)
    return ans

adj = [
    [1, 2],  # Node 0
    [0, 3],  # Node 1
    [0],     # Node 2
    [1],     # Node 3
    []       # Node 4 (disconnected)
]

print(bfs(adj))
