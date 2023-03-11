

ls = [1,7,8]
for i in ls:
    print(i)
    x = 15
    x += 10
    print(x)
print("---------------------------")
for i in range(0,10):
    print(i)
else:
    print("printed")

for i in range(1,101,3):
    print(i)

# break statement
for i in range(1,101):
    print(i)
    if i >= 50:
        break
# continue statement
for i in range(11):
    if i == 6:
        print("6 skipped")
        continue
    print(i)

print("passed")
for i in range(100):
    pass
