def maxDepth(values, index=0):
    if index >= len(values) or values[index] == -1:
        return 0
    left = maxDepth(values, 2 * index + 1)
    right = maxDepth(values, 2 * index + 2)
    return max(left, right) + 1
user_input = input("Enter tree nodes (use -1 for null):")
values = list(map(int, user_input.strip().split()))
print("Maximum depth of Tree:", maxDepth(values))
