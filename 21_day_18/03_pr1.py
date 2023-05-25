'''
ls = [1,2,3]
if 2 in ls:
    print("Present")
else:
    print("Not present")
'''

with open("poem.txt","r") as f:
    content = f.readlines()
    if "twinkel\n" in content:
        print("Yes")
    else:
        print("No")