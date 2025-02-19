class Person:
    """
    A class representing a person with name and age attributes.
    This class demonstrates the usage of dir(), __dict__, and help() methods.
    """
    
    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age
        
    def display_info(self):
        """Display the person's information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

def main():
    # Create a Person instance
    person = Person("John", 30)
    
    # Using dir() to list all attributes and methods
    print("Using dir():")
    print("Attributes and methods of Person instance:")
    for item in dir(person):
        if not item.startswith('__'):  # Filter out dunder methods
            print(item)
    print()
    
    # Using __dict__ to show instance attributes
    print("Using __dict__:")
    print("Instance attributes:")
    print(person.__dict__)
    print()
    
    # Using help() to show documentation
    print("Using help():")
    print("Documentation for Person class:")
    help(Person)

if __name__ == "__main__":
    main()
