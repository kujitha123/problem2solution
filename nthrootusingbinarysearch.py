def nthRoot(n,m):
    low=1
    high=m
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
	        return mid
    	elif(mid**n>m):
	        high=mid-1
	    elif(mid**n<m):
	        low=mid+1
    return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))
	           
 