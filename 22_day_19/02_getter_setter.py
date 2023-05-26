class Emplyee:
    company = "Adidas"
    foundedBy = "ABC Man"
    foundedDate = "1/1/99"
    name = None
    age = None
    salary = 20000
    joinDate = "2/2/2013"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    @getattr
    def printSalry(self):
        print(self.salary)
    @setattr
    def setSalary(self,s):
        self.salary = s


john = Emplyee("Mr John",25)
john.pritSalary()

john.salary = 50000
john.pritSalary()