fullname = ('Grace', 'M', 'Hopper') # what Tuples looks like

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60 
    remaining_seconds = seconds - hours * 3600 - minutes * 60 
    return hours, minutes, remaining_seconds
    
result = convert_seconds(5000)
print(result) # (1, 23, 20)
print(type(result)) # <class 'tuple'> this shows that its as convert_seconds

hours, minutes, remaining_seconds = result  
print(hours, minutes, remaining_seconds) # this way we unpack the tuple into 3 seperat elements

hours, minutes, remaining_seconds = convert_seconds(1000)
print(hours, minutes, remaining_seconds)


# Practice - Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21