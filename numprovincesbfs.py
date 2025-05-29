def BFS(i,visited,q,adjList):
    while(q):
        node=q.pop(0)
        for it in adjList[node]:
            if(visited[it]==0):
                visited[it]=1
                q.append(it)
        ans.append(node)
 def numProvinces(adj,v):
     adjList=[]
     for i in range(v):
         adjList.append([])
     n=len(adj)
     m=len(adj[0])
     for i in range(n):
         for j in range(m):
             if(adj[i][j]==1 and i!=j):
                 adjList[i].append(j)
                 adjListList[j].append(i)
     visited=[0]*v
     c=0
     for i in range(0,v):#loop is for unconnected nodes
          if(visited[it]==0):
                visited[it]=1
                q=[i]
                BFS(i,visited,q,adjList)
                c+=1
          return c                                                                                                                                                                                                                                                     
