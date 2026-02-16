# Python is dynamically typed language,
# which means that you don't have to declare the type of a variable when you create it.
# The type of a variable is determined at runtime based on the value assigned to it.
# Here are some common data types in Python:

# 1. Numeric Types:
# - int: Represents integer values. Example: 42, -7, 0
# - float: Represents floating-point numbers (decimal values). Example: 3.14, -0.001, 2.0
# - complex: Represents complex numbers with a real and imaginary part. Example: 1 + 2j, -3 - 4j
# 2. Sequence Types:
# - list: An ordered, mutable collection of items. Example: [1, 2, 3], ['a', 'b', 'c'], [1, 'hello', 3.14]
# - tuple: An ordered, immutable collection of items. Example: (1, 2, 3), ('a', 'b', 'c'), (1, 'hello', 3.14)
# - range: Represents a sequence of numbers. Example: range(0, 10), range(1, 5, 2)
# 3. Text Type:
# - str: Represents a sequence of characters (string). Example: "Hello, World!", 'Python is great', "12345"
# 4. Mapping Type:
# - dict: Represents a collection of key-value pairs. Example: {'name': 'Alice', 'age': 30}, {'fruit': 'apple', 'color': 'red'}
# 5. Set Types:
# - set: Represents an unordered collection of unique items. Example: {1, 2, 3}, {'a', 'b', 'c'}, {1, 'hello', 3.14}
# - frozenset: Represents an immutable version of a set. Example: frozenset({1, 2, 3}), frozenset({'a', 'b', 'c'}), frozenset({1, 'hello', 3.14})
# 6. Boolean Type:
# - bool: Represents a boolean value, which can be either True or False. Example: True, False
# 7. None Type:
# - NoneType: Represents the absence of a value. Example: None
# You can use the built-in type() function to check the type of a variable. For example:
# Example:
# x = 42
# print(type(x))  # Output: <class 'int'>
# y = "Hello"
# print(type(y))  # Output: <class 'str'>


# creating a program to find the type of data
x = 42
print(type(x))  # Output: <class 'int'>
y = "Hello"
print(type(y))  # Output: <class 'str'>
z = 3.14
print(type(z))  # Output: <class 'float'>
a = [1, 2, 3]
print(type(a))  # Output: <class 'list'>
b = (1, 2, 3)
print(type(b))  # Output: <class 'tuple'>
c = {"name": "Alice", "age": 30}
print(type(c))  # Output: <class 'dict'>
d = {1, 2, 3}
print(type(d))  # Output: <class 'set'>
e = frozenset({1, 2, 3})
print(type(e))  # Output: <class 'frozenset'>
f = True
print(type(f))  # Output: <class 'bool'>
g = None
print(type(g))  # Output: <class 'NoneType'>
