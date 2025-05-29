def subsum(ind, curr, ans, arr, k):
    if ind == len(arr):
        if sum(curr) == k:
            ans.append(curr.copy())
        return
    curr.append(arr[ind])
    subsum(ind + 1, curr, ans, arr, k)
    curr.pop()
    subsum(ind + 1, curr, ans, arr, k)
    return ans

arr = list(map(int, input().split()))
k = int(input())
ind = 0
curr = []
ans = []
for lst in ans:
    if(sum(lst)==k):
    return True
return False
print(subsum(ind, curr, ans, arr))


