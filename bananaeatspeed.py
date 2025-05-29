from math import *
def KoKoEat(arr,k):
        low=1
        high=max(arr)
        while(low<=high):
            noOfBanana=(low+high)//2
            time=0
            for num in arr:
                time+=ceil(num/noOfBanana)
            if(time<=k):
                high=noOfBanana-1
            else:
                low=noOfBanana+1
        return low
arr=list(map(int,input().split()))
k=int(input())
print(KoKoEat(arr,k))