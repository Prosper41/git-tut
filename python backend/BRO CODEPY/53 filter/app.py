friends = [
    ('Rick', 21),
    ('lola', 12),
    ('kay', 22),
    ('chander', 32),
    ('ross', 89),
    ('rose', 17),
    ('franca', 16)
]
age = lambda data:data[1] >= 18
drinking_age = list(filter(age, friends))
for i in drinking_age:
    print(i)
 