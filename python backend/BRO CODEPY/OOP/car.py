class Car:
    def __init__(self, make,model, color, year):

        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def drive(self):
        print('This ' +self.model +' car is driving')

    def stop(self):
        print('This car ' +self.model+ ' is stopped')
