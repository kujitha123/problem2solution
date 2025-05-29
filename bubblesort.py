# push the max element to the last by doing adjacency swap element
def BubbleSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr        
arr=list(map(int,input().split()))       
print(BubbleSort(arr))
            