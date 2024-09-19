"""
Description:
    This program implements a simple calculator for 4 basic operations:
    addition, subtraction, multiplication, and division. Each operation takes
    two integer parameters (operands) and returns the result.
"""
 
# Functions for the 4 operations
 
# Addition
def add(a, b):
    return a + b
 
# Subtraction
def subtract(a, b):
    return a - b
 
# Multiplication
def multiply(a, b):
    return a * b
 
# Division (with handling for division by zero)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
 
 
# Example usage of the calculator functions
if __name__ == "__main__":
    # Example operands
    num1 = 10
    num2 = 5
 
    # Outputs for each operation
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide(num1, num2)}")