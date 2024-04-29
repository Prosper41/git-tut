try:
    numerator = int(input('Enter a number to divide: '))
    denomintor = int(input('Enter a number to divide: '))

    result = numerator / denomintor
except ZeroDivisionError as e:
    print(e)
    print('You can\'t divide by Zero! Jon')
except ValueError as e :
    print(e)
    print('Enter only Number')
except Exception as e:
    print(e)
    print('something went wrong :( ')
else:
    print(result)
finally:
    print('execution done')
    
