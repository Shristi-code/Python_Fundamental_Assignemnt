""" In control_structures.py, write a function classify_number:
○ Prompt the user to enter a number.
○ Use if statements to classify the number as positive, negative, or zero.
○ Use a while loop to allow the user to classify additional numbers until they type
"exit."
 """
 # control_structures.py

def classify_number():
    while True:
        # Prompt the user to enter a number or type 'exit' to quit
        user_input = input("Enter a number (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        # Try to convert the input to a float and classify the number
        try:
            number = float(user_input)
            if number > 0:
                print("The number is positive.")
            elif number < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function
classify_number()