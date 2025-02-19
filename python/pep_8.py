def calculate_sum(numbers):
    """
    Calculate the sum of numbers in a list.

    Args:
        numbers (list): A list of numbers to sum

    Returns:
        float: The sum of all numbers in the list
    """
    total = 0
    for number in numbers:
        total += number
    return total


def format_name(first_name, last_name):
    """
    Format a full name from first and last name.

    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name

    Returns:
        str: Formatted full name
    """
    return f"{first_name.title()} {last_name.title()}"


class Student:
    """A class to represent a student."""

    def __init__(self, name, age, grade):
        """Initialize student attributes."""
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        """Return formatted student information."""
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


# Example usage
numbers = [1, 2, 3, 4, 5]
total = calculate_sum(numbers)
print(f"Sum of numbers: {total}")

full_name = format_name("john", "doe")
print(f"Formatted name: {full_name}")

student = Student("Alice Smith", 20, "A")
print(student.get_info())
