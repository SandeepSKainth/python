# Learning the concept of formatting
# Formatting is a way to control how the output of a program is displayed. 
# It allows us to specify the layout, alignment, and precision of the output.
# In Python, we can use the format() method to format strings.
# The format() method takes one or more arguments and formats them according to the specified format string.
# The format string can contain placeholders that are replaced by the arguments passed to the format() method.
# Placeholders are defined using curly braces {} and can contain format specifiers to control the formatting of the output.
# For example, if we want to format a number to have two decimal places, we can use the format specifier :.2f inside the curly braces.
# Here is an example of using the format() method to format a string:
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# In this example, the placeholders {} are replaced by the values of name and age, resulting in the output "My name is Alice and I am 30 years old."
# We can also specify the order of the arguments by using numbers inside the curly braces. For example:
formatted_string = "My name is {0} and I am {1} years old. {0} is a nice name.".format(name, age)
print(formatted_string)
# In this example, the first placeholder {0} is replaced by the value of name, and the second placeholder {1} is replaced by the value of age. The output will be "My name is Alice and I am 30 years old. Alice is a nice name."
# We can also use named placeholders by using variable names inside the curly braces. For example:
formatted_string = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string)
# In this example, the placeholders {name} and {age} are replaced by the values of the variables name and age, resulting in the output "My name is Alice and I am 30 years old."
# The format() method also allows us to specify the alignment and width of the output. For example, if we want to align a string to the left and specify a width of 20 characters, we can use the format specifier :<20 inside the curly braces.
formatted_string = "Name: {:<20} Age: {}".format(name, age)
print(formatted_string)
# In this example, the name is left-aligned and takes up 20 characters, while the age is displayed normally. The output will be "Name: Alice                Age: 30"                


name = input("Enter your name: ")
age = input("Enter your age: ")
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)