import os

# os.rename
# os.remove

# another way
# from os import *

try: 
    os.mkdir("Test") 
except:
    print("Directory already exists")
finally:
    os.chdir("./Test")
    os.mkdir("newdir")
    os.chdir("newdir")
    #os.rename("testfile.txt", "demo.txt")