def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    return length * width

def greet(name):
    """
    Prints a greeting message with the given name.
    
    Args:
        name (str): The name of the person to greet
    """
    print(f"Hello, {name}!")

# Example usage with docstrings
print(calculate_area.__doc__)  # Print the docstring of calculate_area function
print("\n")
print(greet.__doc__)  # Print the docstring of greet function

# Using the functions
area = calculate_area(5, 3)
print(f"Area of rectangle: {area}")

greet("Alice")
