
f = open("dummy.txt","r")
print(f.readlines())
#
#
#
f.close()

f2 = open("dummy.txt","w")
text = "My neme is dash dash"
f2.write(text)
f2.close()



