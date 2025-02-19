from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fibonacci(n):
    """Calculate nth Fibonacci number with caching"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_without_cache(n):
    """Calculate nth Fibonacci number without caching"""
    if n < 2:
        return n
    return fibonacci_without_cache(n-1) + fibonacci_without_cache(n-2)

def main():
    # Test with caching
    print("Testing fibonacci with caching:")
    start = time.time()
    result = fibonacci(35)
    end = time.time()
    print(f"Result: {result}")
    print(f"Time taken with caching: {end - start:.4f} seconds\n")

    print("Testing fibonacci with caching:")
    start = time.time()
    result = fibonacci(35)
    end = time.time()
    print(f"Result: {result}")
    print(f"Time taken with caching: {end - start:.4f} seconds\n")

    # Test without caching
    print("Testing fibonacci without caching:")
    start = time.time()
    result = fibonacci_without_cache(35)
    end = time.time()
    print(f"Result: {result}")
    print(f"Time taken without caching: {end - start:.4f} seconds\n")

    # Demonstrate cache info
    print("Cache information:")
    print(fibonacci.cache_info())

if __name__ == "__main__":
    main()
