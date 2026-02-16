# Diffrent ways to define variables in python
# 1. Using assignment operator
x = 10
y = "Hello"
z = 3.14
# 2. Multiple assignment
a, b, c = 1, "World", 2.718
# 3. Using the same value for multiple variables
m = n = o = 5


# 4. Using a function to define a variable
def get_greeting():
    return "Hello, World!"


greeting = get_greeting()
# 5. Using input to define a variable
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Swapping values of two variables
x = 5
y = 10
print("Before swapping: x =", x, "y =", y)
x, y = y, x
print("After swapping: x =", x, "y =", y)

# Using input to swap values of two variables
a = input("Enter the first value: ")
b = input("Enter the second value:")

print("Before swapping a =", a, "b =", b)
a, b = b, a
print("After swapping a =", a, "b =", b)
