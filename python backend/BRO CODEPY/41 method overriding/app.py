class Animal:

    def eat(Self):
        print('Tis eating')

class Rabbit(Animal):
    def eat(self):
        print('This rabbit is a carrot')
        

rabbit = Rabbit()
rabbit.eat()