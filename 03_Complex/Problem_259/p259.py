import os.path
import time

t = os.path.getctime("myfile.csv")
ctime = time.ctime(t)
print(ctime)