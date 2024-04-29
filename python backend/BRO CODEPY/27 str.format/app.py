animal = 'cow'
item = 'moon'

# print('The '+animal+' jumped over the '+item)

# print('The {} jumped over the {}'.format(item, animal))
# print('The {} jumped over the {}'.format('moon', 'cow'))

# text = 'The {} jumped ocver the {}'
# print(text.format(animal, item))

name = 'Prosper'

# print("hello, my name is {}".format(name))
# print("hello, my name is {:10}. Nice to meet you.".format(name)) #adding padding

# print("hello, my name is {:<10}. Nice to meet you.".format(name)) #left aligning

# print("hello, my name is {:>10}. Nice to meet you.".format(name)) #right aligning


# FORMATTING NUMBER VARIABLES
pi_number  = 3.12341
number = 1000
print('The number pi is {:.2f}'.format(pi_number))
print('The number  is {:,}'.format(number))
print('The number  is {:b}'.format(number))
print('The number  is {:o}'.format(number))
print('The number  is {:X}'.format(number))
print('The number  is {:e}'.format(number))