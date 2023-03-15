fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi") # append add an item to the end of the list 
print(fruits)    
fruits.insert(0, "Orange") # 0 is location of where we want to add the element - or
print(fruits)   
fruits.insert(100, "Peach") # when you use number larger than the list it will simply add it at the end
print(fruits)
fruits.remove("Melon")
print(fruits)
#fruits.remove("Pear") this will cause an Error because there is no such thing in the list to remove
#print(fruits)
fruits[2] = "Strawberry"
print(fruits)

#results
['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi', 'Peach']
['Orange', 'Pineapple', 'Banana', 'Apple', 'Kiwi', 'Peach']
['Orange', 'Pineapple', 'Strawberry', 'Apple', 'Kiwi', 'Peach']