temp = int(input('what is the temp outside: '))

if not (temp >= 0 and temp <= 30):
    print('bad temp today')
elif  not (temp < 0 or temp > 30):
    print('the temp is good today')
    print('outside')
