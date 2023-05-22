# Calculator
from art import logo
print(logo)

# Functions for the calc.
# Add


def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Dictionary
operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}


num1 = int(input("What's the first number? "))

for operation in operations:
    print(operation)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number? "))


calc_func = operations[operation_symbol]

answer = calc_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


for operation in operations:
    print(operation)
operation_symbol = input("Pick an operation from the line above: ")

num3 = int(input("What is the next number? "))
calc_func = operations[operation_symbol]
answer2 = calc_func(answer, num3)

print(f"{answer} {operation_symbol} {num3} = {answer2}")
