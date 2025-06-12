def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
nnn = int(input("Enter how many Fibonacci numbers to generate: "))
fibonacci_numbers = generate_fibonacci(nnn)
print(f"The first {nnn} Fibonacci numbers are:")
print(fibonacci_numbers)
