class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent class's __init__ using super()
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        # Call parent class's speak method using super()
        super().speak()
        print(f"{self.name} barks: Woof!")
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

def main():
    # Create a Dog instance
    dog = Dog("Max", "Golden Retriever")
    
    # Call methods
    dog.display_info()
    dog.speak()
    
    # Demonstrate inheritance and super() usage
    print("\nChecking inheritance:")
    print(f"Is dog an instance of Dog? {isinstance(dog, Dog)}")
    print(f"Is dog an instance of Animal? {isinstance(dog, Animal)}")

if __name__ == "__main__":
    main()
