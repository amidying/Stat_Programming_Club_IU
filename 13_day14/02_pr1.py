
x1 = int(input("Enter num1: "))
x2 = int(input("Enter num2: "))
x3 = int(input("Enter num3: "))

# def Max(a,b):
#     if a>b:
#         return a
#     return b
# print(Max(x1,Max(x2,x3)))

def maxOfThree(a,b,c):
    if a>b and a>c:
        return a
    elif b > c:
        return b
    return c
print(maxOfThree(x1,x2,x3))

print(max(x1,x2,x3))