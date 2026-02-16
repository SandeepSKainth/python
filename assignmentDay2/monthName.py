# writing a program to print the month name based on the month number
while True:
    month_number = input("Enter the month number (1-12): ")
    if month_number.lower == "exit":
        print("Exiting the program.")
        break
    try:
        month_number = int(month_number)
        if month_number == 1:
            print("January")
        elif month_number == 2:
            print("February")
        elif month_number == 3:
            print("March")
        elif month_number == 4:
            print("April")
        elif month_number == 5:
            print("May")
        elif month_number == 6:
            print("June")
        elif month_number == 7:
            print("July")
        elif month_number == 8:
            print("August")
        elif month_number == 9:
            print("September")
        elif month_number == 10:
            print("October")
        elif month_number == 11:
            print("November")
        elif month_number == 12:
            print("December")
        else:
            print("Please enter a valid month number between 1 and 12.")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")
