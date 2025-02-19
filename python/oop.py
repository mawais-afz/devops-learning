class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self.__age = value
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Grade must be a number")
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.__grade = value
        
    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade}")
        
    def has_passed(self):
        return self.grade >= 60

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"

def main():
    # Create student objects
    student1 = Student("John", 15, 85)
    student2 = Student("Emma", 16, 55)
    
    # Display student information using getters
    print("Student 1 Information:")
    print(f"Name: {student1.name}")
    print(f"Age: {student1.age}")
    print(f"Grade: {student1.grade}")
    print(f"Passed: {student1.has_passed()}\n")
    
    print("Student 2 Information:")
    print(f"Name: {student2.name}")
    print(f"Age: {student2.age}") 
    print(f"Grade: {student2.grade}")
    print(f"Passed: {student2.has_passed()}")
    
    # Demonstrate setters
    print("\nUpdating student information...")
    student1.name = "John Smith"
    student1.age = 16
    student1.grade = 90
    
    print("\nUpdated Student 1 Information:")
    print(f"Name: {student1.name}")
    print(f"Age: {student1.age}")
    print(f"Grade: {student1.grade}")
    print(f"Passed: {student1.has_passed()}")

    # Demonstrate method overriding with __str__
    print("\nDemonstrating method overriding with __str__:")
    print(f"Student 1: {student1}")
    print(f"Student 2: {student2}")

if __name__ == "__main__":
    main()
