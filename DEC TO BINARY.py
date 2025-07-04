n = int(input("Enter a decimal number: "))

# Convert to binary using bin() and remove '0b' prefix
binary = bin(n)[2:]

print(f"Binary equivalent: {binary}")
