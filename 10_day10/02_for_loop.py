# print(end=" ")
# by default end = "\n"

for i in range(100):
    print(i)


for i in range(1, 101,2):
    print(i)

for i in range(0,101,2):
    print(i," ",end = "\t")
    print()

# Generating a list using loop
ls = []
for i in range(100):
    ls.append(i)
print(ls)
# accessing element of a list using loop
for i in ls:
    print(i+5)

l = len(ls)
for i in range(l):
    print(ls[i])
print("List printed successfully")

# for loop with else
for i in range(10):
    print(i)
else:
    print("Done")

# for loop continue statement
for i in range(1,6):
    if i == 3:
        print("i ==3 ")
        continue
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("-----------------------------------------")
# Break Statement

for i in range(10):
    if i == 5:
        break
    print(i)

# out of 1000 candidates find 10 candidates whose cgpa is above 3.5

# pass
for i in ls:
    pass

print("Passed")
