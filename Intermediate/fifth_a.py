# Events and Daemon Threads

import threading

# Events
event = threading.Event()

def myfunction():
    print("Waiting for Event to trigger!...")
    # wait until event is triggered
    event.wait()
    print("Performing action XYZ now...")

t1 = threading.Thread(target = myfunction )
t1.start()

x = input("Do you want to trigger to event? (y/n): ")
if x == "y":
    event.set()


# Output
# 88665a1bbda3:Intermediate khuparag$ python3 fifth.py
# Waiting for Event to trigger!...
# Do you want to trigger to event? (y/n): y
# Performing action XYZ now...




