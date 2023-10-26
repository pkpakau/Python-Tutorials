### Queues

import queue

# Why to use queues? ( )

q = queue.Queue()

# 1, 2, 3, 4, 5 = in queue
# top contains 1 ( pop )
# now queue looks like
# 2, 3, 4, 5

numbers = [10, 20, 30 ,40, 50, 60, 70]
for number in numbers:
    q.put(number)

# FiFo Queue
print("FiFo Queue")
print(q.get())
print(q.get())
print(q)


# full() or empty() to check status of queue

# Queue act as Stack ( LiFo Queue)
print("Lifo Queue")
q = queue.LifoQueue()
for x in numbers:
    q.put(x)

print(q.get())

# Priority Queue ( provide priority with element, starts with 1 and lower the number, higher the priority)
# pass input as tuple
print("Priority Queue")
q = queue.PriorityQueue()

q.put((2, "Hello, World!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get()[1])