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