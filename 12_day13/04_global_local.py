
# scope of variables
x = 100 # global
def total(a,b):
    # x = 5 # local
    global y
    y = 10

    return a+b+y

print(total(5,1))
print(x)
print(y)