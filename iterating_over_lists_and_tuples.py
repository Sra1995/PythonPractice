animals = ["Lion", "Zebra" , "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "dylan", "Reese"]
for index, person in enumerate(winners):
    print("{}, - {}".format(index + 1, person))
    
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
        return result

print(full_emails([("alex@example.com", "Alex diego"), ("Shay@example.com", "Shay Brandt") ]))


# practice - Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.

def skip_elements(elements):
	element = [] # code goes here
	for index, e in enumerate(elements):
		if index % 2 == 0:
			element.append(e)
	
	return element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']