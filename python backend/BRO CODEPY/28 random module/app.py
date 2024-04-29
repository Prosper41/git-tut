import random

x = random.randint(1, 6)
y = random.random() #generate random floating point

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1, 2, 3, 4, 5, 6, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)

print(cards)