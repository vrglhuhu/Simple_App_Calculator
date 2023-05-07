# Vergel, Chean Bernard Villanueva
# Simple App Calculator

# Print selecting operation
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
                # Ask the user to enter first number  
                # Ask the user to enter second number    
                # Printing result    
            # If the user input other character  
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