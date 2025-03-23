def print_missing_numbers_in_fibonacci(n):
    """
    Print the numbers that do not appear in the first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
    """
    # Generate the first n Fibonacci numbers
    fibonacci = [1, 1]  # Starting with 1, 1 as the first two Fibonacci numbers
    
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    print(f"First {n} Fibonacci numbers: {fibonacci}")
    
    # Find the maximum value to check for missing numbers
    max_value = fibonacci[-1]
    
    # Find and print the missing numbers
    missing_numbers = []
    for num in range(1, max_value + 1):
        if num not in fibonacci:
            missing_numbers.append(num)
    
    print(f"Missing numbers: {missing_numbers}")

# Get input from the user
try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print_missing_numbers_in_fibonacci(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
