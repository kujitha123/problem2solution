arr = list(map(int, input().split()))
k = int(input())
n = len(arr)
ans = []

for i in range(n):
    for j in range(i, n):
        ans.append(arr[i:j+1])

maxLen = 0
for lst in ans:
    if sum(lst) == k:
        if len(lst) > maxLen:
            maxLen = len(lst)

print(maxLen)
