# Programmer & userID = Niyam Acharya & nka42
# Program Date = 11/29/2023
# Description:
# Demonstrates and validates the functionality of the NewStack class.
# Creates a NewStack instance, adds elements, and displays stack operations.
# Tests NewStack methods including push, pop, size checking, and emptiness.
# Acts as a testbed to confirm NewStack's adherence to LIFO behavior.

from stack import NewStack 
# Test script to demonstrate and validate NewStack functionality.

def main():
    print("Testing the implementation of stacks with linked lists")

    print("Here is a brand new stack:")
    print("Empty Stack")
    print()
    # Create an instance of NewStack.
    new_stack = NewStack()

    # Add elements to the stack.
    new_stack.put(10)
    new_stack.put(20)
    new_stack.put(30)
    new_stack.put(40)
    
    # Display stack contents before and after operations.
    print(new_stack)
    
    # Remove elements from the stack and display size and emptiness.
    top_item = new_stack.get()
    print("\nSize of stack:", len(new_stack))
    if top_item is not None:
        print("\nFound at the top:", top_item)
    print("\nNow here is the stack after removing a few values:")
    print(new_stack)

if __name__ == "__main__":
    main()
