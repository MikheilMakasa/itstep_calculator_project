# Defining Calculator class with basic arithmetic operations.
class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        # Check if the second number is zero to avoid division by zero.
        if num2 != 0:
            return num1 / num2
        else:
            return "❗ Error ❗ You can't divide by zero 💣"

# Function to get user input, with input validation for numbers.
def get_input():
    while True:
        try:
            num1 = float(input("📝 Enter your first number: "))
            break
        except ValueError:
            print("❌ Invalid input ❌ Please enter a valid number.")

    operation = input("📝 Enter the operation (+, -, *, /): ")

    while True:
        try:
            num2 = float(input("📝 Enter your second number: "))
            break
        except ValueError:
            print("❌ Invalid input ❌ Please enter a valid number.")

    return num1, operation, num2

# Main function to handle the calculation. 
def calculate():

    # Creating an instance of the Calculator class.
    calculator = Calculator()

    while True:
        # Get user input for the calculation.
        num1, operation, num2 = get_input()

        if operation in ['+', '-', '*', '/']:
            # Performing the  operation based on user input.
            if operation == '+':
                result = calculator.add(num1, num2)
            elif operation == '-':
                result = calculator.subtract(num1, num2)
            elif operation == '*':
                result = calculator.multiply(num1, num2)
            elif operation == '/':
                result = calculator.divide(num1, num2)

            # Display the result of the calculation.
            print(f"✅ Result: {result}")
        else:
            # Display an error message for invalid operations.
            print("❌ Invalid operation ❌ Please enter a valid operation (+, -, *, /).")

# Start the calculation process.
calculate()
