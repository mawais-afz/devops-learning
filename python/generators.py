def fibonacci_generator(n):
    """Generator function that yields n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def even_numbers_generator():
    """Generator function that yields infinite even numbers"""
    n = 0
    while True:
        yield n
        n += 2

def squares_generator(start, end):
    """Generator function that yields squares of numbers from start to end"""
    for num in range(start, end + 1):
        yield num ** 2

def main():
    # Using fibonacci generator
    print("First 8 Fibonacci numbers:")
    fib = fibonacci_generator(8)
    for num in fib:
        print(num, end=" ")
    print("\n")
    
    # Using even numbers generator
    print("First 5 even numbers:")
    even_gen = even_numbers_generator()
    for _ in range(5):
        print(next(even_gen), end=" ")
    print("\n")
    
    # Using squares generator
    print("Squares of numbers from 1 to 5:")
    squares = squares_generator(1, 5)
    for square in squares:
        print(square, end=" ")
    print("\n")

if __name__ == "__main__":
    main()
