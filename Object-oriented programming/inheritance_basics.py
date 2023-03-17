class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        
class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

# fruit is the parent - Apple and Grape are the siblings
# the Fruit in the () is to show the inheritance relationship


granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)

#-------------------------------------------------------------------

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))
        
class Piglet(Animal):
    sound = "Oink!"
    
hamlet = Piglet("hamlet")
print(hamlet.speak())

class Cow(Animal):
    sound = "Moooooo"
    
milky = Cow("Milky white")
print(milky.speak())


#-------------------------------------------------------------------

# practice question mid video

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()


