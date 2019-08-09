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
# create salary getter/setter
# to avoid negative salary
# create Manager class
# implement __str__
# __init__ (self, name, address, salary, numberOfEmployeesBenieth)
#   call super() ...
#   implement __str__  and call super()__str__
