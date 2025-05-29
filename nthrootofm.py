def floorSqrt(n,m):
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            ans=i
            break
        elif(i**n>m):
            break
    return ans
n=int(input())
m=int(input())
print(floorSqrt(n,m))