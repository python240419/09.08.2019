class Animal:
    def __init__(self, name, age):
        self.__name = None # to avoid crash
        self.__age = None # to avoid crash
        self.name = name
        self.age = age
    def __str__(self):
        return f'Animal {self.name} {self.__age}'
    '''
    def getAge(self): # getter
        return self.__age
    def setAge(self, value):
        if value >= 0: # setter
            self.__age = value
    '''
    @property
    def age(self):  # getter
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:  # setter
            self.__age = value
    @property
    def name(self):  # getter
        # how to check if name property exists in object ?
        # if not '_Animal__name' in dir(self):
        #    return None        
        return self.__name
    

    @age.setter
    def name(self, value):
        if len(value) >= 2:  # setter
            self.__name = value

dolphine = Animal('Lucky', 200)
dolphine.age = -200
print(dolphine.name)
