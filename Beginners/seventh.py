### Functions
# ( block of reusable code ) # DRY

def helloworld():
    print("Hello, World!")

helloworld()

def add(x:int, y:int):
    return x + y

print(add(10,20))

# default values of parameters
def add(x = 0, y = 1):
    return x + y

print(add())

# multiple parameters without specifying count
def mysum(*numbers:int ):
    result = 0
    for number in numbers:
        result += number
    return result

print(mysum(10, 20, 30, 40, 50))