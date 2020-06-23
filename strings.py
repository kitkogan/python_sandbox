# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Kit'
age = 36
# Concatenate
print('Hello I am ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
# print('{}, {}, {}'.format('a', 'b', 'c'))
# print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
# print('My name is {name} and I am {age}'.format(name='Kit', age='36'))

# F-Strings (only in 3.6+)
# print(f'my name is {name} and I am {age}')

# String Methods

s = 'hello there world'

# Capitalize 1st letter
print(s.capitalize())

# All upper case
print(s.upper())

# All lower case
print(s.lower())

# Swap case
print(s.swapcase())

# Get Length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alpabetic
print(s.isalpha)

# Is all numeric
print(s.isnumeric) 