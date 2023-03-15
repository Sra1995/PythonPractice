x = {}
print(type(x)) # <class 'dict'>

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts) # print("jpg" in file_counts)
print(file_counts["txt"]) # 14
print("jpg" in file_counts) # True
print("html" in file_counts) # False

file_counts["cfg"] = 8 # how to add to dictionary
print(file_counts)
file_counts["csv"] = 17 # it replaced old value that exist rather than adding to it 
print(file_counts)

# how to delete element from dictionary

del file_counts["cfg"]
print(file_counts) # {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}