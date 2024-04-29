class Prey:
    def flee(self):
        print('this animal flees')

class Predator:
    def hunt(self):
        print('This animal\t HUNT too')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass   

class Fish(Predator, Prey):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
fish.hunt()
fish.flee()
