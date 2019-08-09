class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'name : {self.name}'

class Dog(Animal):
    def __init__(self, name, color):
        # 1. code duplication
        # self.name = name

        # 2. super() -- best!
        super().__init__(name)

        # 3. parent class Name
        #Animal.__init__(self, name)

        self.color = color

    def __str__(self):
        return super().__str__() + f' Dog {self.color} '

rexy = Dog('rexy', 'black')
print(rexy)

# exercise:
# create Employee class
# __init__ (self, name, address, salary)
# create Manager class
# create salary getter/setter
# to avoid negative salary
# implement __str__
# __init__ (self, name, address, salary, numberOfEmployeesBenieth)
#   call super() ...
#   implement __str__  and call super()__str__

class Employee:
    def __init__ (self, name, address, salary):
        self.__salary = None
        self.name = name
        self.address = address
        self.salary = salary
    def __str__(self):
        return f'{self.name} {self.address} {self.salary}'

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value

class Manager(Employee):
    def __init__(self, name, address, salary, numOfEmployees):
        super().__init__(name, address, salary)
        self.numOfEmployees = numOfEmployees
    def __str__(self):
        return super().__str__() + f' {self.numOfEmployees}'

m = Manager("Big boss", "Hertzeliya", 42000, 15)
print(m)
m.salary = -5 # should not change
print(m)
m.salary = m.salary + 4735
print(m)
