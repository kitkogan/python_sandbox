# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Modules
import datetime
from datetime import date #need to add this for date.today() to work
import time
from time import time

# Pip modules
# import camelcase

# Custom
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()

timestamp = time()
print(timestamp)
print(today)

# camel = camelcase.CamelCase()
# text = 'hello there world'
# print(camel.hump(text))

# Ex custom module
email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Not an email')