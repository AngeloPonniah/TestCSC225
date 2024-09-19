def main():
    # Start an infinite loop to continuously prompt the user
    while True:
        # Display the menu of options
        print("Choose an action:")
        print("1: Calculate Addition")
        print("2: Calculate Subtraction")
        print("3: Calculate Product")
        print("4: Calculate Division")
        print("5: Quit")
 
        # Get the user's choice
        choice = input("Enter your choice (1-5): ")
 
        # Check if the user wants to quit
        if choice == '5':
            print("Quitting the calculator. Goodbye!")
            break  # Exit the loop and end the program
 
        # Check if the choice is a valid operation
        if choice in ['1', '2', '3', '4']:
            try:
                # Get two integer inputs from the user
                num1 = int(input("Enter the first integer: "))
                num2 = int(input("Enter the second integer: "))
            except ValueError:
                # Handle invalid input if the user does not enter integers
                print("Invalid input. Please enter integer numbers.")
                continue  # Go back to the beginning of the loop
 
            # Perform the chosen operation
            if choice == '1':
                result = num1 + num2
                operation = "addition"
            elif choice == '2':
                result = num1 - num2
                operation = "subtraction"
            elif choice == '3':
                result = num1 * num2
                operation = "multiplication"
            elif choice == '4':
                # Handle division and check for division by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue  # Go back to the beginning of the loop
                result = num1 / num2
                operation = "division"
 
            # Display the result of the operation
            print(f"The result of the {operation} of {num1} and {num2} is: {result}")
        else:
            # Handle invalid choice
            print("Invalid choice. Please select a valid option (1-5).")
 
# Entry point of the program
if __name__ == "__main__":
    main()