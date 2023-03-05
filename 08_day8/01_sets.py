
# Sets

s = {1,2,3,6,5,4}
print(s)
print(type(s))

s1 =set()
s1.add(154)
s1.add(1457)
s1.add(1)
print(s1)


# Sets methods and functions
ss = {1,8,2,3}
print(ss)
print(len(ss))
ss.remove(1)
print(ss)
ss.pop()
print(ss)
ss.clear()
print(ss)


# union
s1 = {1,2,3,4}
s2 = {3,4,5,6,7}
s = s1.union(s2)
print(s)
s3 = s1.intersection(s2)
print(s3)

