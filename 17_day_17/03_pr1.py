def Maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    return c
def maxOfAList(ls):
    maxi = -999999
    for i in ls:
        maxi = max(maxi,i)
    return maxi
print(Maximum(1,2,3))
print(maxOfAList([10,5,4,100,990999]))