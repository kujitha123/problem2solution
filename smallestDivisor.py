from math import *
def smallestDivisor(arr, k):
    low=1
    high=max(arr)
    while(low<=high):
        div=(low+high)//2
        sum=0
        for num in arr:
            sum+=ceil(num/div)
        if(sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(smallestDivisor(arr,k))