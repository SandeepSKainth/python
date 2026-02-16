# how to take input from user

from datetime import datetime


name = input("Enter your name: ")   
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")

#how to take input from user and convert it to integer
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)   

# Taking input from user and converting it to float
num1 = float(input("Enter the first number: "))     
num2 = float(input("Enter the second number: "))
product = num1 * num2
print("The product of", num1, "and", num2, "is", product)

# Taking input from user and converting it to boolean
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
print("Is the user a student?", is_student) 

# Taking input from user and converting it to a list
numbers = input("Enter a list of numbers separated by commas: ")
number_list = [int(num) for num in numbers.split(",")]
print("The list of numbers is:", number_list)

# Taking input from user and converting it to a tuple
coordinates = input("Enter the coordinates (x, y) separated by a comma: ")
x, y = map(float, coordinates.split(","))
print("The coordinates are: x =", x, "y =", y)      

# Taking input from user and converting it to a dictionary
person_info = input("Enter your name and age separated by a comma: ")
name, age = person_info.split(",")
person_dict = {"name": name.strip(), "age": int(age.strip())}
print("The person's information is:", person_dict)      

# Taking input from user and converting it to a set
unique_numbers = input("Enter a list of numbers separated by commas: ")
number_set = set(int(num) for num in unique_numbers.split(","))
print("The set of unique numbers is:", number_set)      

# Taking input from user and converting it to a complex number
real_part = float(input("Enter the real part of the complex number: "))
imaginary_part = float(input("Enter the imaginary part of the complex number: "))
complex_number = complex(real_part, imaginary_part)
print("The complex number is:", complex_number) 

# Taking input from user and converting it to a date
#from datetime import datetime
date_input = input("Enter a date (YYYY-MM-DD): ")           
date_object = datetime.strptime(date_input, "%Y-%m-%d")
print("The date you entered is:", date_object.date())


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)

