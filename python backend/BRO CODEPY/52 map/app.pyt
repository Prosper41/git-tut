store = [
    ("shirt", 20.00),
    ("pants", 24.00),
    ("jacket", 233.00),
    ("socks", 2.00)
]

to_cedis = lambda data: (data[0], data[1]*13)
store_cedis =list(map(to_cedis, store))
for x in store_cedis:
    print(x)
    
print('')

to_dollars = lambda data: (data[0], data[1]/13)
store_dollars =list(map(to_dollars, store))
for i in store_dollars:
    print(i)

 