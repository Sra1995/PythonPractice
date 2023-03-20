cat software.csv
# name, version, statues, users
# row 1
# row 2
# row 3
with open('software.csv') as software:
    reader = csv.DictReader(sfotware)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))
        
# MailTree has 324 users
# CalDoor has 22 users
# Chatty Chicken has 4 users

# we can use DictWriter in a similar way to generate a CSV file from the contents of a list of dictionaries. This means that each element in the list will be a row in the file, and the values of each field will come out of each of the dictionaries.

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]  # This will help DictWriter() organize the CSV rows properly.
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames= keys)
    writer.writeheader()
    writer.writerrows(users)
    
# then  we write to check how to looks

cat by_department.csv 