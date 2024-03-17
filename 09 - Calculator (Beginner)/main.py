import os
from art import logo


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to add two numbers
def add(n1, n2):
    return n1 + n2


# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2


# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2


# Function to divide two numbers
def divide(n1, n2):
    return n1 / n2


# Dictionary mapping operation symbols to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Main calculator function
def calculator():
    print(logo)

    # Input for the first number
    num1 = float(input("What's the first number?: "))

    should_continue = True

    # Calculator loop
    while should_continue:
        # Display available operations
        for symbol in operations:
            print(symbol)

        # Input for the operation symbol and the next number
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # Perform the calculation using the selected operation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Check if the user wants to continue with the result or start a new calculation
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear_screen()


# Run the calculator
calculator()
