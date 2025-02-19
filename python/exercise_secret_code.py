import random
import string

def encode_word(word):
    if len(word) >= 3:
        # Remove first letter and append to end
        word = word[1:] + word[0]
        # Add 3 random characters to start and end
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=6))
        return random_chars[:3] + word + random_chars[3:]
    else:
        # Reverse the string if less than 3 chars
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        # Reverse if less than 3 chars
        return word[::-1]
    else:
        # Remove 3 random chars from start and end
        word = word[3:-3]
        # Move last char to beginning
        return word[-1] + word[:-1]

def main():
    while True:
        choice = input("Would you like to (C)ode or (D)ecode? ").upper()
        
        if choice not in ['C', 'D']:
            print("Please enter C for code or D for decode")
            continue
            
        message = input("Enter the message: ")
        words = message.split()
        
        if choice == 'C':
            result = ' '.join(encode_word(word) for word in words)
            print("Coded message:", result)
        else:
            result = ' '.join(decode_word(word) for word in words)
            print("Decoded message:", result)
            
        if input("Would you like to try again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
