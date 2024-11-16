import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include special characters ? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for length.")

if __name__ == "__main__":
    main()
