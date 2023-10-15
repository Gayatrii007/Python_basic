import random
import string


# Function to generate a random password
def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Combine character sets based on complexity
    complexity = input("Select complexity (low, medium, high): ").lower()
    if complexity == "low":
        characters = lowercase_letters + digits
    elif complexity == "medium":
        characters = lowercase_letters + uppercase_letters + digits
    elif complexity == "high":
        characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        print("Invalid complexity selection. Using medium complexity.")
        characters = lowercase_letters + uppercase_letters + digits

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Input from the user
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer for the password length.")
