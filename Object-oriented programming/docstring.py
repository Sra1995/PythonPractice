def to_seconds(hours, minutes, seconds):
    """Return the amount of seconds in the given hours, minutes, and seconds.""" # we start it by using 3 qoutation marks and ending it with 3 qoutation marks
    return hours*3600 + minutes*60 + seconds
    
help(to_seconds) # however, when we do this the terminal output will only display the message we wrote

class Piglet:
    """Represents a piglet that can say their name."""
    years = 0 
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18
        
help(Piglet)

# Practice

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)

Here is your output:
Help on class Person in module submission:

class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  greeting(self)
 |      Outputs a message with the name of the person
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


Excellent! You’ve mastered the art of providing info using
docstrings!
