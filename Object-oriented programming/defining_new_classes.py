class Orange:
    pass # basically we create empty class and tell it to pass instead of doing something

class Apple:
    color = "" # can make it empty ""
    flavor = ""

jonoagold = Apple()
jonoagold.color = "red" # assigning value under color
jonoagold.flavor = "sweet"
print(jonoagold.color)

print(jonoagold.flavor)

# Dot notation
# lets you access any of the abilities the object might have (called methods) or information it might store (called attributes)

# i.e.

print(jonoagold.color.upper())

# Practice

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"