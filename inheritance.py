class Animal:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    # override
    def __str__(self):
        return f'Animal {self.name}'

    # not override
    def sayYourName(self):
        pass

class Dog(Animal):
    pass
    def __repr__(self):
        return f'Dog {self.name}'

class Buldog(Dog):
    pass

rexy = Dog('rexy')
print(rexy)
#print(help(Dog))

print(isinstance(rexy, Dog))
print(isinstance(rexy, Animal))
print(isinstance(rexy, Buldog))
print(issubclass(Dog, Buldog))
print(issubclass(Buldog, Dog))

'''
class Point:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        if isinstance(other, Point)
            ...            
p1 = Point()
p2 = Point()
x = p1 + 3
x = p1 + p2
'''
