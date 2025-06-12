def factorial(n):
    if n<0:
        return"factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact
nnn = int(input("enter a number: "))
result = factorial(nnn)
print(f"The factorial of {nnn} is {result}")
