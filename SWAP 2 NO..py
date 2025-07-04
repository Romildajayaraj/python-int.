a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping without third variable
a = a + b
b = a - b
a = a - b

# Output
print(f"After swapping:\na = {a}\nb = {b}")
