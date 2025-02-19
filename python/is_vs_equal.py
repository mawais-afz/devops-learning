# Demonstrating the difference between 'is' and '==' operators

# == compares values
x = [1, 2, 3]
y = [1, 2, 3]
print("x ==  y:", x == y)  # True because values are equal
print("x is y:", x is y)   # False because they are different objects

# 'is' compares object identity
a = [1, 2, 3]
b = a  # b references the same object as a
print("\na == b:", a == b)  # True because values are equal
print("a is b:", a is b)   # True because they are the same object

# Special case with small integers
num1 = 256
num2 = 256
print("\nnum1 == num2:", num1 == num2)  # True
print("num1 is num2:", num1 is num2)   # True (due to integer interning)

# Large integers are not interned
big_num1 = 257
big_num2 = 257
print("\nbig_num1 == big_num2:", big_num1 == big_num2)  # True
print("big_num1 is big_num2:", big_num1 is big_num2)   # False

# String interning example
str1 = "hello"
str2 = "hello"
print("\nstr1 == str2:", str1 == str2)  # True
print("str1 is str2:", str1 is str2)   # True (due to string interning)
