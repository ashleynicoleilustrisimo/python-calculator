def calculator():
    # Get first number
    print("Please enter number")
    x = float(input())
    
    # Get second number
    print("Enter another number")
    y = float(input())
    
    # Display operation choices
    print("\nSelect operation:")
    print("1. Division (X / Y)")
    print("2. Multiplication (X # Y)")
    print("3. Addition (X + Y)")
    print("4. Subtraction (X - Y)")
    
    # Get operation choice
    operation = input("Enter choice (1/2/3/4): ")
    
    # Perform calculation based on choice
    if operation == '1':
        if y != 0:  # Check for division by zero
            result = x / y
        else:
            return "Error: Cannot divide by zero"
    elif operation == '2':
        result = x * y
    elif operation == '3':
        result = x + y
    elif operation == '4':
        result = x - y
    else:
        return "Invalid operation selected"
    
    return f"Result: {result}"

# Run the calculator
if __name__ == "__main__":
    print("Calculator Program")
    print(calculator())
