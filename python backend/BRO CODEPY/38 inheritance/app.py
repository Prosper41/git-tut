class Animal:

    alive = True

    def eat(self):
        print('This animal is eating')

    def slumber(self):
        print('This animal is sleeping')


class Rabbit(Animal):
    def run(self):
        print('This rabbbit is running')


class Fish(Animal):
    def swim(self):
        print('This fish can swim')


class Hawk(Animal):
    def fly(self):
        print('the hawk can fly')


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# rabbit.slumber()

rabbit.run()
fish.swim()
hawk.fly()
