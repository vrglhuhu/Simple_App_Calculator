# Vergel, Chean Bernard Villanueva
# Simple App Calculator

# Import pyfiglet 
import pyfiglet

# Print selecting operation
welcome = pyfiglet.figlet_format("Simple App Calculator".center(55), font="digital")
print(welcome)
print("=" * 110)
print("=" * 110)
print("To select operation.")
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
                # Ask the user to enter first number   
                # Ask the user to enter second number    
                # Printing result   
            # If the user input other character
        # If the user wants multiplication
                # Ask the user to enter first number
                # Ask the user to enter second number
                # Printing result
            # If the user input other character
        # If the user wants division       
                # Ask the user to enter first number
                # Ask the user to enter second number
                # Printing result
            # If the user input other character or zero as the second number
        # Ask user if they want to have another calculation
        # Break the while loop if user answered no
    # If not in the four operations 