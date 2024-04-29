student = ('Yaw', 22, 'male', 22)

print(student.count('Yaw'))
print(student.index(22))

for x in student:
    print(x)

if 'Yaw' in student:
    print('exist')
else:
    print('none bro')