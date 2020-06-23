# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]

print(type(numbers))
print(numbers)

# using a constructor
numbers = list((1,2,3,4,5))
fruits = ['apples', 'oranges', 'grapes', 'pears']

print(numbers)

# Get value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('mangos')

# Remove from list
fruits.remove('grapes')

# Insert at a certain position
fruits.insert(2, 'strawberries')

# Remove from position
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)


