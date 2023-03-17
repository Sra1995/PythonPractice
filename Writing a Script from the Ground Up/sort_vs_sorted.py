numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers) # [1, 2, 4, 6, 7]
names = ["Carlos", "Rayan", "Alexia", "Kayla"]
print(names) # ['Carlos', 'Rayan', 'Alexia', 'Kayla']
print(sorted(names)) # ['Alexia', 'Carlos', 'Kayla', 'Rayan']
print(names) # ['Carlos', 'Rayan', 'Alexia', 'Kayla']
print(sorted(names, key=len)) # ['Rayan', 'Kayla', 'Carlos', 'Alexia']
# unlike sort, sorted is not permenant and only sort for that one instance que