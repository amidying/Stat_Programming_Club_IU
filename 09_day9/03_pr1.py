

a,b = 22,23
c,d = 44,1

if a>b and b>c and c>d:
    print(a)
elif b>c and c>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)

# * Way two

tp = (a,b,c,d)
print(max(tp))
print(max(a,b,c,d))