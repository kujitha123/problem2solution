#sorted and rotated array
#Rule1:-identify the soreted half(low val<=mid) then check target exists in that half and repeat same
#Rule2:-check whether the element exists in the sorted half or not
#code:
def search(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        #left half sorted
        elif(arr[low]<=arr[mid]):
            if(arr[low]<=key<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        #right half soretd    
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=list(map(int,input().split()))
key=int(input())
print(search(arr,key))                