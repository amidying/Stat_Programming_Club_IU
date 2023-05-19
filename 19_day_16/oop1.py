

class Employee():
    name = "Unknow"
    idNu = 0
    salary = 0
    def __init__(self,name,idNu,salary):
        self.name = name
        self.idNu = idNu
        self.salary = salary
    
    # method
    def getName(self):
        print(f"{self.name}")
        return self.name
    def getSalary(self):
        print(f"{self.salary}")
    

Rabbi = Employee("Rabbi",542,554)
Neaz = Employee("Neaz",45,124)

print(Rabbi.name)
print(Neaz.name)

Nayeem = Employee("Nayeem",14,4875)
Nayeem.getName()