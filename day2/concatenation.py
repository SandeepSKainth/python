# Concatenation of strings in Python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# Concatenating first name and last name to create a full name
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Concatenating strings with numbers
age = input("Enter your age: ")
# Concatenating age with a string to create a message
message = "You are " + age + " years old."
print(message)

# Concatenating multiple strings
greeting = "Hello"
name = "Alice"
welcome_message = greeting + ", " + name + "!"
print(welcome_message)

# Using the join method for concatenation
words = ["Python", "is", "awesome"]
sentence = "".join(words)
print(sentence)
# Using f-strings for concatenationdd

name = "Bob"
age = 30
info = f"My name is {name} and I am {age} years old."
print(info)



#name = saab
age = 25
salary = 50000

print(age+salary)
