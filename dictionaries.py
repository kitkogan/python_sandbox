# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dicionary
person = {
    'first_name': 'Jay',
    'last_name': 'Cat',
    'age': 40
}

# Using a constructor
# person = dict(irst_name='John', last_name='Doe', age=30)

# Access value
print(person['first_name'])
print(person['last_name'])

# Add key/value
person['phone'] = '555-555-5555'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'minneapolis'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Length
print(len(person2))

# Clear
person.clear()

print(person)

# list of dictionaries
people = [
    {'name': 'KitKit', 'age': 10},
    {'name': 'Ezzie', 'age': 1},
]
print(people[1]['name'])

