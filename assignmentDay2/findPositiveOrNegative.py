# find the number is positive or negative

while True:
    userinput = input("Enter a number (or type 'exit' to quit): ")
    if userinput.lower() == "exit":
        print("Exiting the program.")
        break
    try:
        number = float(userinput)  # Check if the input can be converted to a float

        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
