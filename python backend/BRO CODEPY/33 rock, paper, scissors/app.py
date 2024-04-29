import random

choices = ['rock', 'paper', 'scissors']
player = None

computer = random.choices(choices)
while player not in choices:
    player = input('rock, paper, or scissors: ').lower()

if player == computer:
    print('computer: ', computer)
    print('player: ', player)
    print('Tie ')
elif player == 'rock':
    if computer == 'Paper':
        print('computer: ', computer)
        print('player: ', player)
        print('You lose!')
    if computer == 'scissors':
        print('computer: ', computer)
        print('player: ', player)
        print('You win!')
elif player == 'scissors':
    if computer == 'Paper':
        print('computer: ', computer)
        print('player: ', player)
        print('You lose!')
    if computer == 'scissors':
        print('computer: ', computer)
        print('player: ', player)
        print('You win!')



# INCOMPLETE GAME