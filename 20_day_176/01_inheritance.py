class Animal:
    name = "Animal"
    category = "Something"
    def __init__(self,name,category):
        self.name= name
        self.category = category
    
    def which_class(self):
        return self.name
    def speak(self):
        return print("Speak")
    

class Dog(Animal):
    legs = 4
    
    # def __init__(self, name, category):
    #     super().__init__(name, category)
    def __init__(self,legs):
        self.legs = legs
    def speak(self):
        print("Bark")


# class AsianDog(Dog):

# a = Animal("Any","Any")
# a.name
# d = Dog(4)
# d.name
# d.speak()
D = Dog(423)

print(type(D))
print(type(3))
print(type("amr"))