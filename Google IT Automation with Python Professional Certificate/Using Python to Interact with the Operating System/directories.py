print(os.getcwd())
#home/user
os.mkdir("new_dir")
os.chdir("new_dir")
os.getcwd()
#'/home/user/new_dir'


#-------------------------------------------------------------------

import os 
os.listdir("website")
#['images', 'index.html', 'favicon.ico']
dir = "website"
for name in os.lisdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):   # By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
        
# result would be:
# website/images is a directory
# website/index.html is a file
# website/favicon.ico is a file 

# protip - In Linux and MacOS, the portions of a file are split using a forward slash(/). On Windows, they're split using a backslash(\).