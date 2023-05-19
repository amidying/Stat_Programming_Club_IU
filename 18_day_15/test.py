# import os
# print(os.listdir())

# f = open("dummy.txt","r")
# print(f.readline())
# print(f.readlines())

# f.close()

text = "this is just text"
with open("dummy.txt","a") as f:
    f.write(text)

with open("dummy.txt","w") as f:
    f.write(text)

with open("dummy5.txt","w") as f:
    f.write(text)