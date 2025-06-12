def is_narcissistic(number):
    # Convert the number to a string to easily get digits and count
    digits = [int(d) for d in str(number)]
    num_digits = len(digits)
    
    # Calculate the sum of digits raised to the power of num_digits
    total = sum(d ** num_digits for d in digits)
    
    # Check if the total equals the original number
    return total == number

# Example usage
num = int(input("Enter a number: "))
if is_narcissistic(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
