
def pattern_print(n):
    for i in range(n+1):
        print("* "*(n-i))
def patter_2(n):
    while n >0:
        print("* "*n)
        n-=1
    
pattern_print(5)
patter_2(5)