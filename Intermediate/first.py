# Classes and objects

# class Person:
#     def __init__(self):
#         print("Hello from Init/Constructor")
#         self.name = 'Parag'
#         self.age = 25
#         self.height = 174

class Person():

    # class variable
    amount = 0
    # Constructor
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

        # class variable alteration
        Person.amount += 1

    # class method contains self keyword as first parameters
    def hello_world(self):
        print("Hello from hello_world() function!")

    # delete method defines what happens when object gets deleted
    def __del__(self):
        print("Object deleted")
        Person.amount -= 1

    # what happens when we print our object ( default, it only gives object id and location in memory)
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    # class methods example
    def get_older(self, years):
        self.age += years

person1 = Person('Parag', 25, 174)
print(Person.__init__)

person1.name = "papu"

print(person1.name)
print(person1.age)
print(person1.height)
# print no of objects
print(Person.amount)

# class method calling
print(person1.hello_world())

# print object
print(person1)

person2 = Person("bob", 30, 183)
print(Person.amount)

# delete a object in python
del person1

