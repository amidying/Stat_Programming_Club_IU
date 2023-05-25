'''
f = open("this.txt","r")
# print(f.readlines())
content = f.read(15)
print(content)
f.close()
'''

'''
f2 = open("this.txt","r")
print(f2.readline())
f2.close()

'''

# Binary Files

f = open("this","wb")
f.write("This")
f.close()