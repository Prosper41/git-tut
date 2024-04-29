import time
import datetime
# import datetime


# print(time.ctime(10030000))
# print(time.time())
# print(time.ctime(time.time())) #to get the current date and time

# tim3 = time.localtime()
# tim3 = time.gmtime()
# print(tim3)
# localetime = time.strftime("%B %d %Y %H:%M:%S", tim3)
# print(localetime)


# time_str = '17 April, 2024'
# time_obj = time.strptime(time_str, "%d %B, %Y")
# print(time_obj)

time_tup = (2024, 4, 17, 4, 20, 1, 0, 0, 0)
time_str = time.asctime(time_tup)
# print(time_str)

