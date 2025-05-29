def AssignCookie(g, s):
    s.sort()
    g.sort()
    left=0
    right=0
    n=len(s)
    m=len(g)
    while(left<n and right<m):
        if(s[left]>=g[right]):
            left+=1
            right+=1
        else:
            left+=1
    return right
s = list(map(int, input("Enter cookie sizes: ").split()))
g = list(map(int, input("Enter greed factors: ").split()))
print(AssignCookie(g, s))
        
