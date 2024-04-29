# a func that accepts functions as an argument
def loud(txt):
    return txt.upper()

def quite(txt):
    return txt.lower()

def hello(func):
    txt = func('hello')
    print(txt)

hello(loud)
hello(quite)


# returns a function
def divisor(x):
    def dividend(y):
        return x / y 
    return dividend

divide = divisor(2)
print(divide(10))