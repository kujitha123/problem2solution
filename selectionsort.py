
def selectionSort(arr,n):
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i] 
    return arr   
arr=list(map(int,input().split()))
n=len(arr)
print(selectionSort(arr,n))        