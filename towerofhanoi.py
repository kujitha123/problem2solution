def towerofhanoi(n, src, target, auxiliary):
    if n == 1:
        return 1
    moves1 = towerofhanoi(n - 1, src, auxiliary, target)
    moves2 = towerofhanoi(n - 1, auxiliary, target, src)
    return moves1 + 1 + moves2
n=int(input())
src=input()
target=input()
auxiliary=input()
print(towerofhanoi(n, src, target, auxiliary))