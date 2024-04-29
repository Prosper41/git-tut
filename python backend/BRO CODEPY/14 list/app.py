food = ['fufu', 'waakye', 'chessecake', 'coffee', 'wa']

food[0] = 'cakes'

food.append('ice cream')
food.remove('wa')
food.pop()
food.insert(0, 'snack')
food.sort()
food.clear()

for x in food:
    print(x)