class Orange:
    pass # basically we create empty class and tell it to pass instead of doing something

class Apple:
    color = "" # can make it empty ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red" # assigning value under color
jonagold.flavor = "sweet"
print(jonagold.color)

print(jonagold.flavor)

# Dot notation
# lets you access any of the abilities the object might have (called methods) or information it might store (called attributes)

# i.e.

print(jonagold.color.upper())

# Practice

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"
