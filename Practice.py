from Mustang import Mustang

Mustang = Mustang(str(' 420○\n'), 'Ford Mustang 2000\n', 250)

print(Mustang.horse_power, Mustang.model, Mustang.top_speed)

import random

total = 0
for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
        total = total  + i
print(total)


days_in_february = 28
print(str(days_in_february) + 'Days in February')
#
from datetime import datetime, timedelta,timezone
Today = datetime.now()
print('Todeay is: ' + str(Today))
#
One_day = timedelta(days = 1)


yesterday = Today - One_day
#
print('Yesterday Was: ' + str(yesterday))
#
#
Current_date = datetime.now()
#
print('Day: ' + str(Current_date.day))
print('Month: ' + str(Current_date.month))
print('Year: ' + str(Current_date.year))
print('Hours:' + str(Current_date.hour))
print('Seconds:' + str(Current_date.second))
print('Minutes:' + str(Current_date.minute))
#
Birthday = input('When is Your Birthday: (MM/dd/yyyy)?:')
#
Birth_date = datetime.strptime(Birthday, '%m/%d/%Y')
#
print('Birtday: ' + str(Birth_date))
#
#
#
#
#


def Mustang(self):
    print(Mustang)

