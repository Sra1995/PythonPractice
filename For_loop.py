friends = ['Lucas','Blake','Andy', 'Dean']
for friend in friends:
    print("Hi " + friend)
    
#-------------------------------------------------------------------

values = [ 15, 23, 52, 69, 37, 45 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1 

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))