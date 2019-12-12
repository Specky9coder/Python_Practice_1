class my_car:
    def __init__(self, name, Speed = 0):
        self.Speed = Speed
        self.odometer = 0
        self.Kilometer = 10
        self.name = name


    def Mustang(self, mustang_gt):
        mustang_gt.odometer = mustang_gt.Speed



car = my_car('Mustang')
Car = my_car('Gt')
print(car.name)

Car.Mustang(car)

print(car.Speed)
print(car.odometer)
print(car.Kilometer)


