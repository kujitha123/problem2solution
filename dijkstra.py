import heapq
def dijkstra(v,edges,src):
    adjList=[]
    for i in range(v):
        adjList.append([])
    for n,m,w in edges:
        adjList[n].append((m,w))
        adjList[m].append((n,w))
    distance=[float("inf")]*v
    pq=[]
    distance[src]=0
    heapq.heappush(pq,(0,src))
    while (pq):
        dist,node=heapq.heappop(pq)
        for adjnode,adjDist in adjList[node]:
            if(dist+adjDist<distance[adjnode]):
                distance[adjnode]=dist+adjDist
                heapq.heappush(pq,(dist+adjDist,adjnode))
    return distance        
v=4
src=2
edges=[[0,1,1],[1,0,1],[0,2,6],[2,0,6],[1,2,3],[2,1,3],[0,3,2],[3,0,2],[2,3,3],[3,2,3]]
print(dijkstra(v,edges,src))
