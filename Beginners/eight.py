# Exception Handling


# print(9/10)
# x = "text"
# int(x) ( gets errror )

try:
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    print(x / y)
# except :
#     print("There was an error!")

# specific error
except ValueError:
    print("Please enter a valid number next time!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    y = 1
    print(x / y)

# will run anyways
finally:
    print("DONE!")

# ### Raise Exception as part of code
# def some_function():
#     if True:
#         # raise Exception("Something is terribly Wrong!")
#         raise ValueError("Something is terribly wrong!")
    
# some_function()

x = 100
y = 20

assert(x < y)

# Traceback (most recent call last):
#   File "/Desktop/Python NeuralNine Tutorials/Beginners/eight.py", line 38, in <module>
#     assert(x < y)
#            ^^^^^
# AssertionError