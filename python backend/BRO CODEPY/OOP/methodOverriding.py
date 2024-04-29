class Animal:
    def eat(self):
        print('This animal is eating')


class Rabbit(Animal):
    def eat(self):
        print('it is eating a carrot')

rab = Rabbit()
rab.eat()