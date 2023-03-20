#!/user/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    '''This is to check the disk usage by diving free by the total then multipling by 100''' 
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
    
def check_cpu_usage():
    ''' this function check if the cpu usage is less than 75 percent ''' 
    usage = psutil.cpu_percent(1)
    return usage < 75
    
if not check_disk_usage("/") or not check_cpu_usage(): # print error if one of the functions don't work
    print("ERROR!")
else:
    print("Everything is OK!") # print message if both functions wokr and everything is ok
    
    
# once file is saved chmod +x (x for execute) health_check_script.py then ./he to find .py file starting with "he" then ./health_check_script.py
# chmod +_ (r for read, w to write, x to execute instead of '_')