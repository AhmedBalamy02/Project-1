import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols):
    components = ""

    if use_lowercase:
        components += string.ascii_lowercase
    if use_uppercase:
        components += string.ascii_uppercase
    if use_numbers:
        components += string.digits
    if use_symbols:
        components += string.punctuation

    if not components:
        print("Please select at least one component for the password.")
        return None

    password = ''.join(random.choice(components) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the length of the password: "))
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)
    if password:
        print("Your generated password is:", password)

# Start the password generator
password_generator()

