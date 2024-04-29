# squre = []
# for i in range(1, 11):
#     squre.append(i * i)
# print(squre)

# same code as the above code with one line of code
# squre = [i * i for i in range(1, 11)]
# print(squre)




students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 0]
pass_stud = list(filter(lambda x: x >= 43, students))
# print(pass_stud)
            # OR 
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 0]
pass_stud = [i if i >= 45 else "failed" for i in students]
print(pass_stud)


