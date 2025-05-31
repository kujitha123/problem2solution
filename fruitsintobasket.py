##fruits into basket###
#max length subarray with atmost 2 types of number
#brute force solution##
def fruitsbasket(fruits):
    n=len(fruits)
    maxLen=0
    for i in range(0,n):
        s=set()
        for j in range(i,n):
            s.add(fruits[j])
            if(len(s)>2):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
fruits=list(map(int,input().split()))
print(fruitsbasket(fruits))

##optimal code(sliding window concept)##
def fruitsbasket(fruits):
    n=len(fruits)
    left=0
    right=0
    maxLen=0
    d={}
    while(right<n):
        if(fruits[right] in d):
            d[fruits[right]]+=1
        else:
            d[fruits[right]]=1
        if(len(d)>2):
            while(len(d)>2):
                d[fruits[left]]-=1
                if(d[fruits[left]]==0):
                    del d[fruits[left]]
                left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
fruits=list(map(int,input().split()))
print(fruitsbasket(fruits))