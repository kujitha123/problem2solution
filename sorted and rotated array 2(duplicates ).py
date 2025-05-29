def search(arr,key):
        n=len(arr)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==key):
                return True
            if(arr[low]==arr[mid]==arr[high]):
                low+=1
                high-=1
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
        return False
arr=list(map(int,input().split()))
key=int(input())
print(search(arr,key)) 
