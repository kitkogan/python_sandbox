# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'Kit'    # string
# rulz = True     # bool

# Multiple assignment
x, y, name, rulz = (1, 2.5, 'Kit', True)
print(x, y, name, rulz)

# Basic math
a = x + y

# Check type 
print(type(name))
print(type(rulz))

# Casting-- changes var type
x = str(x)
print(type(x))