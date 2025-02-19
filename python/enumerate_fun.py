# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Using enumerate to get both index and value
print("Fruits with their indices:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\nFruits with custom starting index:")
# Using enumerate with a custom starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit #{index}: {fruit}")

# Using enumerate with a list of tuples
inventory = [
    ("Apple", 5),
    ("Banana", 8), 
    ("Cherry", 12)
]

print("\nFruit inventory:")
for index, (fruit, quantity) in enumerate(inventory):
    print(f"{index}. {fruit}: {quantity} pieces")
