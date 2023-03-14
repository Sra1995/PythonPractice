name = "Jack"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print(f"Hello {name}, your lucky number is {number}")
print("Your lucky number is {number, {name}.".format(name=name, number=len(name)*3))


def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#-------------------------------------------------------------------

price = 7.5 
with_tax = price * 1.09 
print(price, with_tax) # results 7.5 8.175 <- this is wrong there is no such thing is half a penny

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax)) # should get Base price: $7.50. With Tax: $8.18

# .2f means float number with two decimals
