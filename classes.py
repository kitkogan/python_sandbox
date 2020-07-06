# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Customer Class

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# Init user object
kit = User('Kit K', 'test@test.com', 36)
jay = User('Jay C', 'jay@test.com', 40)
print(kit.name)
print(jay.email)

# Edit property
kit.age = 20

jay.has_birthday()

# Call method
print(jay.greeting())

# Edit Customer
ezzie = Customer('Ezzie KC', 'ezzie@test.com', 1)

ezzie.set_balance(500)

print(ezzie.greeting())
