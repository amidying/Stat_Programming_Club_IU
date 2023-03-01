from math import sqrt

ls = [1,2,3,4,5]
print(ls)
ls.pop()
print(ls)
ls.pop(2)
print(ls)


# x= (-b+-sqrt(b^2-4ac))/2a

# a = 5
# b = 2
# c = -10
a = float(input("Enter a:"))
b = float(input("Enter b"))
c = float(input("Enter c: "))

x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
print(x1,x2)
print("Value error.")


km = 100
m = km*100
print(km,"km is = ",m,"meter")