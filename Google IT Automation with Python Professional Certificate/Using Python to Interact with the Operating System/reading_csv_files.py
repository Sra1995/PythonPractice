cat csv_file.txt
# name , phone number, job title
# name , phone number, job title
# name , phone number, job title
# name:  , phone: , Role: 
import csv 
f = open("csv_file.txt")
csv_f = csv.reader(f)  # The reader() function of the CSV module will interpret the file as a CSV.
for now in csv_f:
    name, phone, role = row
    print("name: {}, Phone: {}, Role: {}".format(name, phone, role))

# name:  , phone: , Role: 
# name:  , phone: , Role: 
# name:  , phone: , Role: 
# name:  , phone: , Role: 
# name:  , phone: , Role: 

f.close()
