# Function to perform arithmetic operations
def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Invalid operation."

# Input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Calculate and display the result
    result = perform_calculation(num1, num2, operation)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
