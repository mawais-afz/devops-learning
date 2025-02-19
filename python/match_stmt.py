# Example of match statement (Python 3.10+)
def check_status(status):
    match status:
        case "200":
            return "OK - Request successful"
        case "404":
            return "Error - Page not found"
        case "500":
            return "Error - Internal server error"
        case _:
            return "Unknown status code"

# Test the function with different status codes
test_status = "404"
result = check_status(test_status)
print(f"Status {test_status}: {result}")

# Another example with different data types
def process_data(data):
    match data:
        case str():
            print(f"Got a string: {data}")
        case int() | float():
            print(f"Got a number: {data}")
        case list():
            print(f"Got a list with {len(data)} items")
        case _:
            print("Got something else")

# Test with different types
process_data("Hello")
process_data(42)
process_data([1, 2, 3])
process_data({"key": "value"})
