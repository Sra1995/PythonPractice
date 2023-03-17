# Modules : Used to organize functions, classes, and othe rdata together in a structured way

import random
print(random.randint(1, 10)) # I got 9

print(random.randint(1, 10)) # I got 9

print(random.randint(1, 10)) # I got 1

#-------------------------------------------------------------------

import datetime
now = datetime.datetime.now()

print(type(now)) # print(random.randint(1, 10))
print(now) # prints out current time year-month-day HH:MM:SS.Miliseconds

print(now)
2019-04-24 16:54:55.155199
>>> now.year
2019
>>> print(now + datetime.timedelta(days=28))
2019-05-22 16:54:55.155199