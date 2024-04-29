class Car:

    def turn_on(self):
        print('You start the engine')
        return self
    
    def drive(self):
        print('Drive the car')
        return self

    def brake(self):
        print('step on the breaks')
        return self
    
    def turn_off(self):
        print('turn off the engine')
        return self

car = Car()

# car.turn_on().drive()

# car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
