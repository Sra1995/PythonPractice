x = ["Now", "We", "are", "cooking!"]
print(type(x)) # this will state the class like <class 'list'>
print(x) # this would just simply print the list as is ["Now", "We", "are", "cooking!"]
print(len(x)) # this will list how many items in the list in this case 4
print("are" in x) # true or false on whether an item is in the list
print("Today" in x) # False because it is not an item in the list
print(x[0]) # using index to list first item 
print(x[3]) # using index to list fourth item 
print(x[1:3]) # to print a slice of the list - will result in ["We", "Are"]
print(x[:2]) # this will list anything below 2 - will result in ["Now", "we"]
print(x[2:]) # this will list from 2 and above - will result in ["are", "cooking"]


# in Ubuntu I can just type whats in the () and it will give me the result except for like print(x) 


# practice - Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1. 

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split() # sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1]) # added word [n-1]
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


