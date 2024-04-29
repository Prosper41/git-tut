# ----------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print('----------------------------')
        print(key)
        for i in option[question_num-1]:
            print(i)
        
        guess = input('Enter (A, B, C, or D):  ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
# ----------------------------
def check_answer(answer, guess):

    if answer == guess:
        print('Correct')
        return 1
    else:
        print('wrong')
        return 0
# ----------------------------
def display_score(correct_guesses, guesses):
    print('----------------------------')
    print('RESULT')
    print('----------------------------')
    print('Guesses: ', end='')
    for i in guesses:
        print(i, end='')
    print()
# ----------------------------
def play_again():
    pass
# ----------------------------

question = {
    'who created python: ': 'A',
    'what year was python created': 'B',
    'Python was attributed  to which comedy group: ': 'C',
    'Is the earth round: ': 'A'
}

option = [['A. Van ', 'B. Elon musk', 'C. Gates', 'D. Mark'],
    ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. lonley Island', 'B. smosh', 'C. Monty Python', 'SNL'],
    ['A. True', 'B. False', 'Sometimes', 'D. What\'s Earth']]

new_game()