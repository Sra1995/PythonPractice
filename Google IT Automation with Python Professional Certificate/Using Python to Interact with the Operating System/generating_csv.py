hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv','w') as hosts_csv:  # The file must be open, preferably using with open() as, and write permissions must be given. 
    writer = csv.writer(hosts_csv) # write row, which we'll write one row at a time; and write rows, which we'll write all of them together.
    write.writerows(hosts)
    

cat hosts.csv 
# "workstation.local", "192.168.25.46"
# "webserver.cloud", "10.2.5.6"