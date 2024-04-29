import functools

# letter = ["h", "e", "l", "l", "o"]
# word = functools.reduce(lambda x, y :x + y,letter)
# print(word)
factorial = [5, 4, 3, 2, 1]
res = functools.reduce(lambda x, y :x * y,factorial)
print(res)
