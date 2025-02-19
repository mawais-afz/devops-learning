# Basic lambda examples
square = lambda x: x**2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

# Map numbers to their squares
squared_numbers = list(map(square, numbers))
print("Squared numbers:", squared_numbers)

# Sort a list of tuples by second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted pairs:", sorted_pairs)

# Using lambda in list comprehension with conditional
conditional_squares = [square(n) if is_even(n) else n for n in numbers]
print("Conditional squares:", conditional_squares)
