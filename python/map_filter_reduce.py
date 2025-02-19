from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = lambda x: x**2
is_even = lambda x: x % 2 == 0
add = lambda x, y: x + y
# Using map() to square each number
squared = list(map(square, numbers))
print("Squared numbers:", squared)

# Using filter() to get even numbers
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

# Using reduce() to calculate sum of all numbers
sum_all = reduce(add, numbers)
print("Sum of all numbers:", sum_all)

# Combining map, filter and reduce:
# 1. Filter even numbers
# 2. Map them to their squares
# 3. Reduce to get their sum
result = reduce(add, 
               map(square, 
                   filter(is_even, numbers)))
print("Sum of squares of even numbers:", result)
