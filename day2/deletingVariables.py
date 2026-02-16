# Writing programs that delete variables is a good way to learn how to use the del statement.
# The del statement can be used to delete a variable from memory.
# This is useful when you want to free up memory or when you want to remove a variable that is no longer needed.
# Deleting a variable is done using the del statement followed by the variable name.
# For example, if you have a variable x that you want to delete, you can use the following code:
x = 10
print("Before deleting x:", x)
del x
# After deleting x, trying to access it will result in a NameError
try:
    print("After deleting x:", x)
except NameError:
    print("x has been deleted and is no longer accessible.")
# You can also delete multiple variables at once by separating their names with commas.
a = 5
b = 10
print("Before deleting a and b: a =", a, "b =", b)
del a, b
try:
    print("After deleting a and b: a =", a, "b =", b)
except NameError:
    print("a and b have been deleted and are no longer accessible.")
# It's important to note that once a variable is deleted, it cannot be accessed again unless it is redefined.


s = "Hello, World!"
print("Beforer deleting s =", s)
del s
try:
    print("After deleting s =", s)
except NameError:
    print("s has been deleted and is no longer accessible.")
