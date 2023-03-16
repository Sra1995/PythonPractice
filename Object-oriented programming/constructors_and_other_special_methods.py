# learning Constructor

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        
jonagold = Apple("red", "sweet")
print(jonagold.color)

# practice question 

# Want to see this in action? In this code, there's a Person class that has an attribute name, which gets set when constructing the object. 
# Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 
# 2) when the greeting() method is called, the greeting states the assigned name.

# my answer

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Joe Doe")  
# Call the greeting method
print(some_person.greeting())

print(jonagold) # this result in <__main__.Apple object at 0x7feaf3073cd0> but not as an error fix your code kind of thing


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor) 

jonagold = Apple("red", "sweet")

print(jonagold)


