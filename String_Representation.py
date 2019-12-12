class my_car:
# Class.
    def __init__(self, name, Speed = 0):
# Initialization method.
        self.Speed = Speed
        self.odometer = 0
        self.Kilometer = 10
        self.name = name

    # A Method.
    def Mustang(self, mustang_gt):
        mustang_gt.odometer = mustang_gt.Speed
#Preceding (__) and end With (__) it's Called  Dunder Method.
# str is a Overriding a Certain Function .

    def __str__(self):
        return '{}: {}'.format(self.name, self.Kilometer)



# A Object Is a Instance Of  a Class.
# A Object.
car = my_car('Mustang')
Car = my_car('Gt')
print(car)
print(Car)
# print(car.name)
# print(car)
#
Car.Mustang(Car)
#
print()
print()
print()


