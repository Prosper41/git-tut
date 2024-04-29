import os

# path = "C:\\Users\\HP\\OneDrive\\Desktop"
path = "C:\\Users\\HP\\OneDrive\\Desktop"

if os.path.exists(path):
    print('location exist')
    if os.path.isfile(path):
        print('that is a file')
    elif os.path.isdir(path):
        print('that is a folder')
else:
    ('location doesn\'t exist')