def BFS(i,visited,q,adj,ans):
    while(q):
        node=q.pop(0)
        for it in adj[node]:
            if(visited[it]==0):
                visited[it]=1
                q.append(it)
        ans.append(node)
def bfs(adj):
    ans=[]
    v=len(adj)
    visited=[0]*v
    for i in range(0,v):#loop is for unconnected nodes
        if(visited[it]==0):
            visited[it]=1
            q=[i]
            BFS(i,visited,q,adj,ans)
    return ans          
