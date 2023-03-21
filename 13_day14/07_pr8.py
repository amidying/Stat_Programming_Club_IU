

# n = 7 # take it as an input
n = int(input("Enter you num: "))

def multiplicationTable(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")

multiplicationTable(n)