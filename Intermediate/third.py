# Threading

# threads are like light-weighted processes ( like process but consume less resources )
# use same memory and perform better using synchronization between threads

import threading

# def hello_world():
#     print("Hello, World!")

# t1 = threading.Thread(target = hello_world)
# t1.start()

# def function1():
#     for x in range(10000):
#         print("ONE")

# def function2():
#     for x in range(10000):
#         print("TWO")

# t1 = threading.Thread(target = function1)
# t2 = threading.Thread(target = function2)

# t1.start()
# t2.start()

### Waiting for input
def hello():
    for x in range(50):
        print("Hello!")

t1 = threading.Thread(target = hello)
t1.start()

# if you want your threading to be completed first and move on to another statement
# use .join() method
t1.join()

# Print just after threading start and doesn't want above code's execution to be completed!
print("Hello, World after threading")