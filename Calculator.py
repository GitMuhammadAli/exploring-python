def calculator():
    """
    A simple command-line calculator that performs basic arithmetic operations.
    """
    print("Welcome to the Python Calculator!")
    print("Enter 'quit' to exit the calculator at any time.")

    while True:
        num1_str = input("Enter the first number: ")
        if num1_str.lower() == 'quit':
            break
        operator = input("Enter an operator (+, -, *, /): ")
        if operator.lower() == 'quit':
            break
        num2_str = input("Enter the second number: ")
        if num2_str.lower() == 'quit':
            break

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  

        result = 0
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue 
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            continue  

        print(f"Result: {result}")
        print("-" * 20) 
if __name__ == "__main__":
    calculator()
