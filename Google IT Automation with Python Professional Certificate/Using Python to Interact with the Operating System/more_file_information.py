import os 
os.path.getsize("spider.txt")
#192
os.path.getmtime("spider.txt") # this gives timestamp rather than usual time
#157832923.8999994  # this is unix timestamp - it represent seconds since jan 1st
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#datetime.datetime(2020, 1, 6, 7, 2, 3, 899999)


# Practice - Some more functions of the os.path module include getsize() and isfile() which get information on the file size and determine if a file exists, respectively. In the following code snippet, what do you think will print if the file does not exist?

import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")


# answer - False, File not found - Because the file does not exist, getsize() will never be called and our error message will be printed instead.


os.path,abspath("spider.txt")  # The abspath function takes a filename and turns it into an absolute path.
#'/home/user/spider.txt'