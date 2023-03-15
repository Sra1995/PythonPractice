# 1 - Simple List comprehension

#For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. 
#This single line of code iterates over a range from 1 to 10, multiplies each element in the range by 2, and creates a new list from all multiples of 2 from 2 to 20.

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)]) 



### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)


# Click Run to compare the two results.
List comprehension result:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Long form code result:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2 - List Comprehension with Conditional Statement

#You can also use conditionals with list comprehensions to build even more complex and powerful statements.
#You can do this by appending an if statement to the end of the list comprehension.
#For example, [ x for x in range(1,101) if x % 10 == 0 ] generates a new list containing all the integers divisible by 10 from 1 to 100.
#The if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, the number is added to a new list.

### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines 
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)


# Click Run to observe the two results.

List comprehension result:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Long form code result:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# practice Exercise - This exercise will walk you through how to write a list comprehension to create a list of squared numbers (n*n).
#It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].


def squares(start, end):
    square = [n**2 for n in range(start, end+1)] # I wrote this line
    return square # I wrote square 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
