def floorSqrt(n):
    ans=0
    for i in range(1,n+1):
        if(i*i<=n):
            ans=i
        else:
            break
    return ans
n=int(input())
print(floorSqrt(n))