try:
    # Get input from user
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Print multiplication table
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

except ValueError:
    print("Please enter a valid integer number")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("\nTable printed successfully!")
finally:
    print("Program execution completed")
