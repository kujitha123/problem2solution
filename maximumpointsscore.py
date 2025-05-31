def maxScore(cardpoints,k):
  n=len(cardpoints)
  left=0
  right=k-1
  leftSum=sum(cardpoints[left:right+1])
  rightSum=0
  maxSum=leftSum
  rightIndex=n-1
  for i in range(k-1,-1,-1):
    leftSum-=cardpoints[i]
    rightSum+=cardpoints[rightIndex]
    maxSum=max(maxSum,leftSum+rightSum)
    rightIndex-=1
  return maxSum
cardpoints=list(map(int,input().split()))
k=int(input())
print(maxScore(cardpoints,k))