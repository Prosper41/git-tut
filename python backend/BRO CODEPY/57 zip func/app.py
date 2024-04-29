# userName = ['slave', 'master', 'Jerkins']
# password= ['pass@word', 'abcd123', 'qui,@ts']

# users = zip(userName, password)
# for x in users:
#     print(x)



# userName = ['slave', 'master', 'Jerkins']
# password= ['pass@word', 'abcd123', 'qui,@ts']
# users = dict(zip(userName, password))
# for key,value in users.items():
#     print(key+": "+value)



userName = ['slave', 'master', 'Jerkins']
password= ['pass@word', 'abcd123', 'qui,@ts']
login_date = ['1/1/20', '1/09/2024', '3/08/2022']

users = zip(userName, password, login_date)
for i in users:
    print(i)
    