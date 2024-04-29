def add(*nike):
    sum = 0
    nike = list(nike)
    nike[0] = 1
    for i in nike:
        sum += i
    return sum



print(add(21, 12, 12,))

