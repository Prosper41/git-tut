class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


    def drive(self):
        print('This '+self.model+  '  is driving')

    def stop(self):
        print('Tis car' +self.model+  ' stopped') 


car_1 = Car('ford', 'mustang', 2022, 'black')
car_2 = Car('Massada', 'Jass', 1992, 'pink')

print(car_1.make)
print(car_1.year)
print(car_1.model)
print(car_1.color)

car_2.drive()
car_2.stop()