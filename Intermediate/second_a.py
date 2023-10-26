# Inheritance

class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)
    
    def get_older(self, years):
        self.age += years
    

class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker,self).__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12
    
    # Overriding the parent class method
    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text

# person1 = Person("Parag", 25, 174)
# person1.get_older(7)
# print(person1.age)

worker1 = Worker('Bob', 32, 184, 3000)
print(worker1)
print(worker1.salary)
print(worker1.calc_yearly_salary())