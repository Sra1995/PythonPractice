import shutil # for disk usage

du = shutil.disk_usage("/")
print(du) #usage(total=26374176768, used=9022201856, free=16240189440)

ava = du.free/du.total*100
print(ava)

#-------------------------------------------------------------------
import psutil # for cpu utilization

psutil.cpu_percent(0.1) # 0.0 in 0.1 seconds

psutil.cpu_percent(0.1) # 5.0 

psutil.cpu_percent(0.5) # 1.0

psutil.cpu_percent(0.5) # 0.5 