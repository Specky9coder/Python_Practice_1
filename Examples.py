gpa = float(input('What Is Your Grade Point Average:'))

lowest_grade = float(input('What Is Your Lowest Grade: '))

if gpa >= .85 and lowest_grade >= .70:
   honour_roll = True
else:
   honour_roll = False
#
#
#
if honour_roll:
   print('You Made It To The Honour Roll')
#
from array import array
s  = array()
s.append(98)
s.append(99)
print(s)
Person = {}

Person['First'] = 'Keyur'
Person['Last'] = 'Bhadani'
#
for name in ['Keyur','Purva']:
    print(name)
    for index in range(0,2):
        print(index)
        print(name)
#
names = ['Keyur', 'Purva']

Index = 0

while Index < len(names):
    print(names[Index])
    Index += 1
#
import datetime

def print_time ():
    print('Task Completed')
    print(datetime.datetime.now())
    print()

print_time()

for x in range(0,2):
    print(x)

print_time()
#
def get_initial(name, force_uppercase = True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('Enter Your First name: ')
first_name_initial = get_initial(force_uppercase = True, name = first_name)
first_name_initial = get_initial( force_uppercase =False, name = first_name)
middle_name = input('Enter Your Middle Name : ')
middle_name_initial = get_initial(name = middle_name)

last_name = input('Enter Your Last Name: ')
last_name_initial = get_initial(name = last_name)


print('Your Initials Are:' + last_name_initial + first_name_initial + middle_name_initial)
print('Your Initials Are:' + first_name_initial)

import json
#Creat a dictiionaty object
Person_dict = {'First': 'Specky', 'Last': 'Coder'}
Person_dict['City:'] = 'Amalfi Cost'
# Add aditional key pairs ad need to dictionary

# Creat a Staff Dictionary Which Assigns Role To a Person
Staff_dict = {}
Staff_dict['Data Scientist'] = Person_dict

# Creat a list Of Programming Languages

Skills_list = ['Machine Learning, Artificial Intelligence, Python']
Person_dict['Skills'] = Skills_list


Person_json = json.dumps(Person_dict)
print(Person_json)


import os

os_version = os.getenv('os')
print(os_version)


from dotenv import load_dotenv
load_dotenv()

password = os.getenv('PASSWORD')

print(password)


