# Vergel, Chean Bernard Villanueva
# Simple App Calculator

# Import pyfiglet 
import pyfiglet

# Print selecting operation
welcome = pyfiglet.figlet_format("Simple App Calculator".center(55), font="digital")
print(welcome)
print("=" * 110)
print("=" * 110)
print("\nTo select operation.")
print("Press A: Addition")
print("Press B: Subtraction")
print("Press C: Multiplication")
print("Press D: Division\n")

while True:
    # Ask for the operation that the user wants 
    choice = input("Enter your choice of operation: ")

    # Check if the choice is one among the four operations
    if choice.lower() in ('a', 'b', 'c', 'd'):

        # Calculate the given operation.
        # If the user wants addition
        if choice.lower() == 'a':
            print("ADDITION OPERATION")
            try:
                # Ask the user to enter first number
                num1 = float(input("Enter first number that you want to add: "))
                # Ask the user to enter second number
                num2 = float(input("Enter second number that you want to add: "))
                add = num1 + num2
                # Printing result
                print(num1, "+", num2, "=", add)
            # If the user input other character
            except ValueError:
                print("INVALID INPUT. Please enter a number.")
                continue   

        # If the user wants subtraction  
        elif choice.lower() == 'b':
            print("SUBTRACTION OPERATION") 
            try: 
                # Ask the user to enter first number  
                num1 = float(input("Enter first number that you want to subtract: ")) 
                # Ask the user to enter second number   
                num2 = float(input("Enter second number that you want to subtract: "))
                subtract = num1 - num2 
                # Printing result 
                print(num1, "-", num2, "=", subtract)  
            # If the user input other character
            except ValueError:
                print("INVALID INPUT. Please enter a number.")
                continue

        # If the user wants multiplication
        elif choice.lower() == 'c':
            print("MULTIPLICATION OPERATION")
            try:
                # Ask the user to enter first number
                num1 = float(input("Enter first number that you want to multiply: "))
                # Ask the user to enter second number
                num2 = float(input("Enter second number that you want to multiply: "))
                multiply = num1 * num2
                # Printing result
                print(num1, "*", num2, "=", multiply)
            # If the user input other character
            except ValueError:
                print("INVALID INPUT. Please enter a number.")
                continue

        # If the user wants division  
        elif choice.lower() == 'd': 
            print("DIVISION OPERATION")
            try:     
                # Ask the user to enter first number
                num1 = float(input("Enter first number that you want to divide: "))
                # Ask the user to enter second number
                num2 = float(input("Enter second number that you want to divide: "))
                divide = num1 / num2
                # Printing result
                print(num1, "/", num2, "=", divide)
            # If the user input other character or zero as the second number
            except (ValueError, ZeroDivisionError):
                print("INVALID INPUT. Please enter a non-zero number.")
                continue
            
        # Ask user if they want to have another calculation
        # Break the while loop if user answered no
    # If not in the four operations
    else:
        print("Invalid Input")  