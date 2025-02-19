class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod 
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    # Using static methods without creating an instance
    print("Addition:", Calculator.add(10, 5))
    print("Subtraction:", Calculator.subtract(10, 5))
    print("Multiplication:", Calculator.multiply(10, 5))
    print("Division:", Calculator.divide(10, 5))
    
    # Error handling example
    try:
        print("Division by zero:", Calculator.divide(10, 0))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
