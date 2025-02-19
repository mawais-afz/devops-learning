# Decorators are a powerful feature in Python that allows you to modify the behavior
# of functions or classes without directly changing their source code.

# A decorator is a function that takes another function as an argument and extends
# or modifies its behavior by wrapping it in another function.

# Basic decorator structure:
# def decorator_function(original_function):
#     def wrapper_function():
#         # Code executed before the original function
#         result = original_function()
#         # Code executed after the original function
#         return result
#     return wrapper_function

# Decorators can be applied using the @ symbol (syntactic sugar):
# @decorator_function
# def my_function():
#     pass

# Common uses of decorators include:
# - Logging
# - Timing functions
# - Access control and authentication
# - Caching
# - Input validation
# - Rate limiting


# Example of Python decorators

def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

def split_decorator(function):
    def wrapper():
        result = function()
        return result.split()
    return wrapper

# Applying multiple decorators
@split_decorator
@uppercase_decorator
def greet():
    return "hello world"

# Example of decorator with parameters
def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello {name}!")
    return "Done"

def main():
    # Testing the decorators
    print("Testing multiple decorators:")
    print(greet())  # Will print: ['HELLO', 'WORLD']
    
    print("\nTesting decorator with parameters:")
    say_hello("Alice")  # Will print "Hello Alice!" three times

if __name__ == "__main__":
    main()
