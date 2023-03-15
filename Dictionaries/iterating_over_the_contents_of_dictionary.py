file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)
    
#jpg
#txt
#csv
#py

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))
    
print(file_counts.keys())

print(file_counts.values())

for value in file_counts.values():
    print(value)
    
   
# Complete the code to iterate through the keys and values of the cool_beasts dictionary.
# Remember that the items method returns a tuple of key, value for each element in the dictionary. 
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, arm in cool_beasts.items():
    print("{} have {}".format(animal, arm))
    
    
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0 
        result[letter] += 1 
    return result

print(count_letters("aaaaa"))
print(count_letters("Mountain"))