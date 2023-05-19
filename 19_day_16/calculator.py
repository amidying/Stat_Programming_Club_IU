
# class Calculator():
#     def __init__(self,name,a=0,b=0):
#         self.a = a
#         self.b = b
#         self.name = name
    
#     def Add(self,a,b):
#         print(a+b)
#     def Multiplication(self,a,b):
#         return a*b
#     #
#     #
#     #
#     #

    

# calc = Calculator("Neaz")
# calc.Add(5,10)

# list comprehension
# lambda function

import random
from random import randint
import math as m

# ls = []
# for i in range(100):
#     ls.append(random.randint(1,100))
# print(ls)

ls2 = [random.randint(1,101) for i in range(1,101)]
print(ls2)


ls3 = [randint(1,11) for i in range(1,11) for j in range(1,11)]
print(ls3)



cubic = lambda x: x**3

print(cubic(3))
