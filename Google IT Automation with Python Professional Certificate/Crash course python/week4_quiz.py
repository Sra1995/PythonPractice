#Fill in the blank to complete the “first_character” function. This function should return the first character of any string passed in.  Complete the string operation needed in this function so that input like "Hello, World" will produce the output "H".

def first_character(string):
    t = string[0]
    # Complete the return statement using a string operation.
    return t 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K

#-------------------------------------------------------------------
#Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". This function should:

#   accept a string through the parameters of the function;

#   iterate over the characters in the string;

#   determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);

#   increment the counter;

#   return the count of letters in the string.


def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for letter in string: 
        # Complete the if-statement using a string method. 
        if letter.strip() not in character:
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

#  wrong
# I got 18, 16, 22 - need to 

#-------------------------------------------------------------------
# 3
#Employees at a company shared  the distance they drive to work (in miles) through an online survey. These distances were automatically added by Python to a list called “distances” in the order that each employee submitted their distance. Management wants the list to be sorted in the order of the longest distance to the shortest distance. 

#   Complete the function to sort the “distances” list. This function should:

#   sort the given “distances” list, passed through the function’s parameters; ; 

#   reverse the sort order so that it goes from the longest to the shortest distance;

#   return the modified “distances” list.

def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

#-------------------------------------------------------------------
# 4 

# Fill in the blank to complete the “even_numbers” function. This function should use a list comprehension to create a list of even numbers using a conditional if statement with the modulo operator to test for numbers evenly divisible by 2. The function receives two variables and should return the list of even numbers that occur between the “first” and “last” variables exclusively (meaning don’t modify the default behavior of the range to exclude the “end” value in the range). For example, even_numbers(2, 7) should return [2, 4, 6].  
def even_numbers(first, last):
  return [ e for e in range(first, last) if e % 2 == 0 ]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]
#-------------------------------------------------------------------
# 5 

# Fill in the blanks to complete the “car_listing” function. This function accepts a “car_prices” dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". Each new string should appear on its own line.

def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car in car_prices: 
    result += "A {} costs {}".format(car, car_prices[car]) + "\n" # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

#-------------------------------------------------------------------

#6 

# Tessa and Rick are hosting a party. Before they send out invitations, they want to add all of the people they are inviting to a dictionary so they can also add how many guests each friend is bringing to the party.  

#Complete the function so that it accepts a list of people, then iterates over the list and adds all of the names (elements) to the dictionary as keys with a starting value of 0. Tessa and Rick plan to update these values with the number of guests their friends will bring with them to the party. Then, print the new dictionary.

#This function should:

#   accept a list variable named “guest_list” through the function’s parameter;

#   add the contents of the list as keys to a new, blank dictionary;

#   assign each new key with the value 0;

#   print the new dictionary.

def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for gg in guest_list: # Iterate over the elements in the list 
        result[str(gg)] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

#-------------------------------------------------------------------
# 7 

#A teacher is using a dictionary to store student grades. The grades are stored as a point value out of 100.  Currently, the teacher has a dictionary setup for Term 1 grades and wants to duplicate it for Term 2. The student name keys in the dictionary should stay the same, but the grade values should be reset to 0.

#Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will produce a resulting dictionary that contains  “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should: 

#   accept a dictionary “old_gradebook” variable through the function’s parameters;

#   make a copy of the “old_gradebook” dictionary;

#   iterate over each key and value pair in the new dictionary;

#   replace the value for each key with the number 0;

#   return the new dictionary.

def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  new_gradebook = {}
    # Complete the for loop to iterate over the new gradebook. 
  for gg in old_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
    new_gradebook.update({gg:0}) 
  return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}


#-------------------------------------------------------------------

# 8 

# What do the following commands return when 
animal = "Hippopotamus"?
print(animal[3:6])
print(animal[-5])
print(animal[10:])

pop, t, Us

#-------------------------------------------------------------------

# 9 What does the list "colors" contain after these commands are executed?

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

['red', 'white', 'yellow', 'blue'] = answer

#-------------------------------------------------------------------
#10
# What do the following commands return?

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()


answer = dict_keys(['router', 'localhost', 'google'])

