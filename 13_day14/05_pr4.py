

# n = int(input("Enter n:"))

def patternPrint(n):
    for i in range(n+1):
        print("* "*(n-i))

patternPrint(5)