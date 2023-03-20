with open("spider.txt") as file:
    for line in file:
        print(line.upper())
        
#THE ITSY BTSY SPIDER CLIMBED UP THE WATERSPOUT.

# DOWN CAME THE RAIN 

# AND WASHED THE SPIDER OUT. 

# What's happening is that the file has a new line character at the end of each line. So when Python reads the file line by line, the line variable will always have a new line character at the end. In other words, the newline character is not removed when calling read line.

# to avoid getting new empty lines we can use strip() like this

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

#THE ITSY BTSY SPIDER CLIMBED UP THE WATERSPOUT.
#DOWN CAME THE RAIN 
#AND WASHED THE SPIDER OUT. 

# Practice - Can you identify which code snippet will correctly open a file and print lines one by one without whitespace?

with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())
	    
	    
# Another way we can work with the contents of the file is to read the file lines into a list. Then, we can do something with the lists like sort contents. To do that, we open the file and use the.readlines method

 file = open("spider.txt")
 lines = file.readlines()
 file.close()
 lines.sort()
 print(lines)
 
 # output would be like ['Down came the rain\n', 'Out came the sun\n', etc] - \n is backspace
 # Python uses escape sequences with backslash, like \n. Another common escape sequence is \t, for tab.