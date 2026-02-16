# How to handle conditional statements in Python
# Conditional statements are used to perform different actions based on different conditions.
# In Python, we use if, elif, and else statements to handle conditional statements.
# The if statement is used to test a specific condition. If the condition is true, 
# the code block under the if statement is executed.
# The elif statement is used to test additional conditions if the previous conditions were false.
# The else statement is used to execute a block of code if all the previous conditions were false.
# Here is an example of using conditional statements in Python:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))  
num3 = int(input("Enter the third number: "))
if num1>num2 and num1>num3:
    print(num1, "is the greatest number.")
elif num2>num1 and num2>num3:
    print(num2, "is the greatest number.")
elif num3>num1 and num3>num2:
    print(num3, "is the greatest number.")
else:
    print("All numbers are equal.")