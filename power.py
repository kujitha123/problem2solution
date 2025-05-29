def power(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    if n == 0:
        return 1
    if n % 2 == 1:
        return x * power(x, n - 1)
    return power(x * x, n // 2)   
x=int(input("enter a base:"))
n=int(input("Enter a exponent:"))
print(power(x,n))


