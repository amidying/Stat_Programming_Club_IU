def SumN(n):
    if n == 0 or n == 1:
        return n
    return n+SumN(n-1)
SumN(5)