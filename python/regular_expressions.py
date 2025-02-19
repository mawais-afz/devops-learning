import re

def demonstrate_regex():
    """Demonstrate various regex patterns and operations"""
    # Basic pattern matching
    text = "The quick brown fox jumps over the lazy dog"
    pattern = r"fox"
    match = re.search(pattern, text)
    print(f"Found '{pattern}' at position: {match.start() if match else 'Not found'}")

    # Using character classes
    phone_numbers = [
        "123-456-7890",
        "1234567890",
        "(123) 456-7890",
        "123.456.7890"
    ]
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    print("\nValidating phone numbers:")
    for number in phone_numbers:
        print(f"{number}: {'Valid' if re.match(phone_pattern, number) else 'Invalid'}")

    # Email validation
    emails = [
        "user@example.com",
        "invalid.email@",
        "user.name@domain.co.uk",
        "@invalid.com"
    ]
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    print("\nValidating email addresses:")
    for email in emails:
        print(f"{email}: {'Valid' if re.match(email_pattern, email) else 'Invalid'}")

    # Finding all matches
    text = "Python is awesome. Python is powerful. Python is readable."
    matches = re.findall(r'Python', text)
    print(f"\nFound '{matches[0]}' {len(matches)} times in the text")

    # String substitution
    censored = re.sub(r'Python', '****', text)
    print(f"Censored text: {censored}")

def main():
    demonstrate_regex()

if __name__ == "__main__":
    main()
