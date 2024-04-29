from car import Car

car1 = Car('Hyundai', 'Honda', 'black', 2022)
car2 = Car('Ford', 'Mustang', 'blue', 2023)

print(car2.make)
print(car2.year)
print(car2.color)
print(car2.model)

car1.drive()
car2.stop()