##brute force solution##
def maxSubArray(nums):
    n=len(nums)
    maxSum=float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            Sum=sum(nums[i:j+1])
            maxSum=max(maxSum,Sum)
    return maxSum
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

##optimal(kadnes algorithm)##
#In kadens algorithm while adding any elements it gives negative values it converts or changes that number to Zero
def maxSubArray(nums):
    n=len(nums)
    maxSum=float("-inf")
    currentSum=0
    for i in nums:
        currentSum+=i
        maxSum=max(maxSum,currentSum)
        if(currentSum<0):
            currentSum=0
    return maxSum
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
