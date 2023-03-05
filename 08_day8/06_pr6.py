

p1 = input("enter your name: ")
l1 = input("Enter your fav lang: ")
p2 = input("enter your name: ")
l2 = input("Enter your fav lang: ")
p3 = input("enter your name: ")
l3 = input("Enter your fav lang: ")
p4 = input("enter your name: ")
l4 = input("Enter your fav lang: ")
S = {}
S.update({p1:l1})
S.update({p2:l2})
S.update({p3:l3})
S.update({p4:l4})

name = input("Enter your name: ")
print("Your fav lang is: ",S[name])
