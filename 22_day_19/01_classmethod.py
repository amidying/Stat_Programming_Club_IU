class A:
    name = "Unknow"
    age = 23
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printName(self):
        print(self.name)

    @classmethod
    def printAge(self):
        pass
    @property
    def printName(self):
        pass


a = A("ABC",23)

a.printName()
a.printName()
