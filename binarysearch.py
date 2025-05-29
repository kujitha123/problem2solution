#binary search the array is soretd
def binarysearch(arr, k):
    def getLowerBound(arr,k):
        low=0
        high=len(arr)-1
        ans=0
        while(low<=high):
            mid
        n=len(arr)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==k):
               lb=getLowerBounf(arr,k)
            elif(k>arr[mid]):
                low=mid+1
            elif(k<arr[mid]):
                high=mid-1
        rerurn -1  
arr=list(map(int,input().split()))
k=int(input())
print(binarysearch(arr,k))