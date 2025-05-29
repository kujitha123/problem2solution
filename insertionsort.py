#Insertion sort is a simple sorting algorithm that works by building a sorted array one element at a time. It divides the input array into two parts: sorted and unsorted.
def insertionSort(arr):
        n=len(arr)
        for i in range(0,n):
            while(i>0 and arr[i-1]>arr[i]):
                arr[i-1],arr[i]=arr[i],arr[i-1]
                i-=1
        return arr
arr=list(map(int,input().split()))
print(insertionSort(arr))   

# words reverse of string 
s="hey hi hello"
s=s.split(" ")
s=s[::-1]
print(*s) # for convert to string  or print(" ".join(s))

# power of 2 

