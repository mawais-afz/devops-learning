# Creating sets
fruits = {"apple", "banana", "orange", "mango", "apple"}  # Note: duplicates are automatically removed
numbers = set([1, 2, 3, 4, 5])

# Demonstrating set properties
print("Original fruits set:", fruits)
print("Length of fruits set:", len(fruits))

# Adding and removing elements
fruits.add("pineapple")
print("After adding pineapple:", fruits)

fruits.remove("banana")  # Will raise error if element doesn't exist
print("After removing banana:", fruits)

fruits.discard("kiwi")  # Won't raise error if element doesn't exist

# Set operations
vegetables = {"carrot", "tomato", "potato"}
food = fruits.union(vegetables)  # or fruits | vegetables
print("\nAll food items:", food)

# Checking membership
print("\nIs apple in fruits?", "apple" in fruits)
print("Is kiwi in fruits?", "kiwi" in fruits)

# Set methods demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet operations:")
print("Intersection:", set1.intersection(set2))  # or set1 & set2
print("Union:", set1.union(set2))  # or set1 | set2
print("Difference (set1 - set2):", set1.difference(set2))  # or set1 - set2
print("Symmetric difference:", set1.symmetric_difference(set2))  # or set1 ^ set2

print("Update set1 with set2:", set1.update(set2))

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print("\nSquares of numbers 1-5:", squares)


