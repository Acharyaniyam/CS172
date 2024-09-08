# CS 172 - Lab 6: Stack Math
# Authors: Niyam Acharya
# UserIDs: nka42
# Description: This script provides a simple postfix calculator using a Stack data structure. 
# The user can input postfix expressions, and the script will evaluate and display the results.

from stackclass import Stack

def postfix(exp):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    # Split the expression into tokens using spaces as separators
    tokens = exp.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # If the token is a number (including negative numbers), push it onto the stack
            stack.push(float(token))
        elif token in operators:
            # If the token is an operator, pop the top two numbers from the stack and apply the operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            # Push the result back onto the stack
            stack.push(result)
        else:
            # Invalid token in the expression
            print("Invalid token:", token)
            return None

    # The final result should be on top of the stack
    if not stack.isEmpty():
        return stack.top()
    else:
        print("Invalid expression: Empty stack")
        return None

# Main script
if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter 'exit' to quit")

    while True:
        expression = input("Enter Expression: ")
        if expression.lower() == 'exit':
            break
        result = postfix(expression)
        if result is not None:
            print(f"Result: {result}")
