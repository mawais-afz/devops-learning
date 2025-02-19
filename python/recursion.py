def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

def fibonacci(n):
    """
    Calculate the nth number in the Fibonacci sequence using recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print("Factorial examples:")
for i in range(6):
    print(f"Factorial of {i} is: {factorial(i)}")

print("\nFibonacci examples:")
for i in range(8):
    print(f"Fibonacci number at position {i} is: {fibonacci(i)}")
