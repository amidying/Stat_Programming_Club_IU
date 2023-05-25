
'''
f = open("this2.txt","w")
f.write("that")
f.close()
'''

with open("this2.txt","a") as f:
    f.write("\nthis and that")
