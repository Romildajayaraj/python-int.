# Input: Take number from user
n = int(input("Enter a number to print its multiplication table: "))

# Output: Multiplication table from 1 to 10
print(f"Multiplication Table for {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
