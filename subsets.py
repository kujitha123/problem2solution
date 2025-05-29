def subsets(ind, curr_arr, ans, nums):
    if ind == len(nums):
        ans.append(curr_arr.copy())
        return
    curr_arr.append(nums[ind])
    subsets(ind + 1, curr_arr, ans, nums)
    curr_arr.pop()
    subsets(ind + 1, curr_arr, ans, nums)
    return ans
nums = list(map(int, input().split()))
ind = 0
curr_arr = []
ans = []
print(subsets(ind, curr_arr, ans, nums))
































































































































    
