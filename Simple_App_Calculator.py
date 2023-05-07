# Vergel, Chean Bernard Villanueva
# Simple App Calculator

# Import pyfiglet 
import pyfiglet

# Print selecting operation
print("=" * 110)
print("=" * 110)
welcome = pyfiglet.figlet_format("Simple App Calculator".center(55), font="digital")
print(welcome)
print("=" * 110)
print("=" * 110)
print("\n\033[40m\033[33mTo select operation.\033[0m")
print("\U0001F6D1 \033[31mPress A: \033[0m Addition")
print("\U0001F6D1 \033[32mPress B: \033[0m Subtraction")
print("\U0001F6D1 \033[33mPress C: \033[0m Multiplication")
print("\U0001F6D1 \033[34mPress D: \033[0m Division\n")

while True:
    # Ask for the operation that the user wants 
    choice = input("\033[40m\033[33mEnter your choice of operation:\033[0m ")

    # Check if the choice is one among the four operations
    if choice.lower() in ('a', 'b', 'c', 'd'):

        # Calculate the given operation.
        # If the user wants addition
        if choice.lower() == 'a':
            print("\U0001F530 \033[40m\033[35mADDITION OPERATION\033[0m \U0001F530")
            try:
                # Ask the user to enter first number
                num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to add:\033[0m "))
                # Ask the user to enter second number
                num2 = float(input("\U0001F4E2  \033[40m\033[34mEnter second number that you want to add:\033[0m "))
                add = num1 + num2
                # Printing result
                print("\U0001F7E5 TOTAL \U0001F7E5")
                print(num1, "+", num2, "=", add)
            # If the user input other character
            except ValueError:
                print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a number.\033[0m")
                continue   

        # If the user wants subtraction  
        elif choice.lower() == 'b':
            print("\U0001F530 \033[40m\033[35mSUBTRACTION OPERATION\033[0m \U0001F530") 
            try: 
                # Ask the user to enter first number  
                num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to subtract:\033[0m ")) 
                # Ask the user to enter second number   
                num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to subtract:\033[0m "))
                subtract = num1 - num2 
                # Printing result 
                print("\U0001F7E5 TOTAL \U0001F7E5")
                print(num1, "-", num2, "=", subtract)  
            # If the user input other character
            except ValueError:
                print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a number.\033[0m")
                continue

        # If the user wants multiplication
        elif choice.lower() == 'c':
            print("\U0001F530 \033[40m\033[35mMULTIPLICATION OPERATION\033[0m \U0001F530")
            try:
                # Ask the user to enter first number
                num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to multiply:\033[0m "))
                # Ask the user to enter second number
                num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to multiply:\033[0m "))
                multiply = num1 * num2
                # Printing result
                print("\U0001F7E5 TOTAL \U0001F7E5")
                print(num1, "*", num2, "=", multiply)
            # If the user input other character
            except ValueError:
                print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a number.\033[0m")
                continue

        # If the user wants division  
        elif choice.lower() == 'd': 
            print("\U0001F530 \033[40m\033[35mDIVISION OPERATION\033[0m \U0001F530")
            try:     
                # Ask the user to enter first number
                num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to divide:\033[0m "))
                # Ask the user to enter second number
                num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to divide:\033[0m "))
                divide = num1 / num2
                # Printing result
                print("\U0001F7E5 TOTAL \U0001F7E5")
                print(num1, "/", num2, "=", divide)
            # If the user input other character or zero as the second number
            except (ValueError, ZeroDivisionError):
                print("\U0001F6A7 \033[31mINVALID INPUT. Please enter an integer or a non-zero number.\033[0m")
                continue

        # Ask user if they want to have another calculation
        next_calculation = input("\U0001F4CC \033[40m\033[33mDo you want to perform another calculation?\033[0m \033[40m\033[34mYES\033[0m or \033[40m\033[34mNO:\033[0m ")
        # Break the while loop if user answered no
        if next_calculation.upper() == "NO":
            print("\n\U0001F504\U0001F504 Closing Program... \U0001F504\U0001F504 Thank you!")
            
            # create a footer
            print("")
            goodbye = pyfiglet.figlet_format("Visit me again", font = "puffy" )
            print (goodbye)
            print("")
            break

    # If not in the four operations
    else:
        print("\U0001F6A7 \033[31mINVALID INPUT!\033[0m")  

