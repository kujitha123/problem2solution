#sliding window not handle for all negative cases so we use hasing technique
def longestSubarray(arr,k):
        n=len(arr)
        d={}
        Sum=0
        maxLen=0
        for i in range(0,n):
            Sum+=arr[i]
            if(Sum==k):
                maxLen=i+1
            rem=Sum-k
            if(rem in d):
                maxLen=max(maxLen,i-d[rem])
            if(Sum not in d):
                d[Sum]=i
        return maxLen
arr= [10, 5, 2, 7, 1, -10]
k=int(input())
print(longestSubarray(arr,k))

