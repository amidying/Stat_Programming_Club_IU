

def factorialFunc(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i # fact = fact*i
    return fact


x = factorialFunc(5)
print(x)
print(factorialFunc(6))
print(factorialFunc(4))

def factorialRec(n):
    if n == 0 or n == 1:
        return 1
    print(n)
    return n*factorialRec(n-1)

print(factorialRec(5))
print(factorialRec(0))
print(factorialRec(1))
def Summation(n):
    if n == 0 or n ==1 :
        return n
    return n+Summation(n-1)
print(Summation(100))
print(Summation(0))