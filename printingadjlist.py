def graph(v,e,edges):
    adjList=[]
    for i in range(v):
        adjList.append([])
    for n,m in edges:
        adjList[n].append(m)
        adjList[m].append(n)
    for lst in adjList:
        lst.sort()
    return adjList
v=int(input())
e=int(input())
edges=[]
for i in range(e):
    lst=list(map(int,input().split()))
    edges.append(lst)
print(graph(v,e,edges))