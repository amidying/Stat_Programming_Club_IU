

def Max(a,b):
    if a>b:
        # return a
        print(a)
        return
    # return b
    print(b)

Max(6,5)

# ------- Default arg ------------

def Sum(x = 0,y = 0):
    return x+y

print(Sum(2,3))

# string concatination 
a = "Ali"
b = "Neaz"
print(a+b)
print(a + str(1722019))


# --------- Recursion---------

def Factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    return n*Factorial(n-1)
def Sum(n):
    if n == 0:
        return n
    return n+Sum(n-1)
def FactorialLoop(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

# print(Factorial(5))
# print(Factorial(1000))
# print(FactorialLoop(1000))
print(Sum(10))
