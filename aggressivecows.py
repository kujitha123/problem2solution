def aggressiveCows(n,stalls, k):
    def canweplace(minDist,stalls,k):
        cows=stalls[0]
        placedcow=1
        for stall in range(1,len(stalls)):
            if(stalls[stall]-cows>=minDist):
                cows=stalls[stall]
                placedcow+=1
            if(placedcow==k):
                return True
        return False
    stalls.sort()
    Min=min(stalls)
    Max=max(stalls)
    if(k==2):
        return Max-Min
    for minDist in range(1,Max-Min+1):
        if(canweplace(minDist,stalls,k)):
            continue
        else:
            return minDist-1
n=int(input())
k=int(input())
stalls=list(map(int,input().split()))
print(aggressiveCows(n,stalls,k))