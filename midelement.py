def midleelement(nums,start,end):
    if start == end:
        return nums[start]
    elif start + 1 == end:
        return nums[start]
    return midleelement(nums, start + 1, end - 1)
nums=list(map(int,input().split()))
print(midleelement(nums,start,end))
    
