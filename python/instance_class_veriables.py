class Student:
    # Class variable shared by all instances
    school_name = "Python High School"
    total_students = 0
    
    def __init__(self, name, grade):
        # Instance variables unique to each instance
        self.name = name
        self.grade = grade
        Student.total_students += 1
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")

def main():
    # Create student instances
    student1 = Student("John", 10)
    student2 = Student("Emma", 11)
    
    print("Student 1 Information:")
    student1.display_info()
    print(f"Total Students: {Student.total_students}\n")
    
    print("Student 2 Information:") 
    student2.display_info()
    print(f"Total Students: {Student.total_students}\n")
    
    # Demonstrate class variable modification
    print("Changing school name...")
    Student.school_name = "Advanced Python Academy"
    
    print("\nAfter school name change:")
    print("Student 1 Information:")
    student1.display_info()
    
    print("\nStudent 2 Information:")
    student2.display_info()
    
    # Demonstrate instance variable modification
    print("\nChanging student1's grade...")
    student1.grade = 11
    
    print("\nAfter grade change:")
    print("Student 1 Information:")
    student1.display_info()
    
    # Note that student2's grade remains unchanged
    print("\nStudent 2 Information:")
    student2.display_info()

if __name__ == "__main__":
    main()
