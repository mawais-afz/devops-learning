class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Overloads the + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overloads the - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overloads the * operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Overloads the == operator"""
        return self.x == other.x and self.y == other.y

def main():
    # Create vector instances
    v1 = Vector(2, 3)
    v2 = Vector(3, 4)
    
    # Test addition
    v3 = v1 + v2
    print(f"Vector Addition: {v1} + {v2} = {v3}")
    
    # Test subtraction
    v4 = v2 - v1
    print(f"Vector Subtraction: {v2} - {v1} = {v4}")
    
    # Test scalar multiplication
    v5 = v1 * 3
    print(f"Scalar Multiplication: {v1} * 3 = {v5}")
    
    # Test equality
    v6 = Vector(2, 3)
    print(f"Equality Test: {v1} == {v6} is {v1 == v6}")
    print(f"Equality Test: {v1} == {v2} is {v1 == v2}")

if __name__ == "__main__":
    main()
