class Piglet:
    pass

hamlet = Piglet()

class Piglet:
    def speak(self):  # this will make it say oink oink for all isinstances
        print("oink oink")

hamlet = Piglet()
hamlet.speak() 

class Piglet:
    name = "piglet"
    def speak(self):
        print("oink! I'm {} Oink!".format(self.name))  # this will make it say oink oink based on name it was assigned to it
        
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

# Variables that have different vlaues for different instances of the same class are called instance variables.

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
        
piggy = piglet()
print(piggy.pig_years()) # should be 0

piggy.years = 2
print(piggy.pig_years()) # 36

#-------------------------------------------------------------------

# Practice

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())


# Calling methods on objects executes functions that operate on attributes of a specific instance of the class. 
# This means that calling a method on a list, for example, only modifies that instance of a list, and not all lists globally. 
# We can define methods within a class by creating functions inside the class definition. These instance methods can take a parameter called 
# self which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot 
# notation, like self.name, which will access the name attribute of that specific instance of the class object.
# When you have variables that contain different values for different instances, these are called instance variables.
