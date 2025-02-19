# Regular arguments
def greet(name):
    print(f"Hello {name}")

# Default arguments
def power(base, exponent=2):
    return base ** exponent

# Keyword arguments
def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

# Arbitrary arguments (*args)
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Arbitrary keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combining different types of arguments
def mixed_args(required, *args, default="default", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

# Example usage:
greet("Alice")

print(power(2))  # Uses default exponent=2
print(power(2, 3))  # Overrides default exponent

student_info(name="Bob", age=20, grade="A")  # Keyword arguments

print(sum_numbers(1, 2, 3, 4, 5))  # Arbitrary arguments

print_info(name="Charlie", job="Developer", country="USA")  # Arbitrary keyword arguments

mixed_args("Hello", 1, 2, 3, default="custom", x=10, y=20)  # Mixed arguments
