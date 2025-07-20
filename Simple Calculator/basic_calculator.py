# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide the first number by the second
def divide(x, y):
    # Check for division by zero
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Print a welcome message when the calculator starts
print("\nWelcome to the Simple Calculator")
print("It is unable to process negative numbers at the moment.")

# Start an infinite loop so the calculator keeps running until the user exits
while True:
    # Print the list of operations the user can choose from
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Ask the user to choose an operation
    choice = input("Enter your choice (1-5): ")

    # If the user chooses 5, break the loop and exit the program
    if choice == "5":
        print("Goodbye!")
        break

    # If the input is not 1 to 4, show an error and go back to the top of the loop
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    # Ask the user to input the first number
    num1 = input("Enter first number: ")
    # Ask the user to input the second number
    num2 = input("Enter second number: ")

    # Checks if both inputs are valid numbers (including decimals)
    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        print("Please enter valid numbers.")
        continue

    # Convert both inputs from string to float (decimal-friendly)
    num1 = float(num1)
    num2 = float(num2)

    # Based on the user’s choice, call the correct function
    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)

    # Display the result of the operation
    print(f"Result: {result}")