
with open("dummy2.txt","w") as f:
    text3 = "m is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy "
    f.write(text3)

with open("dummy2.txt","a") as f:
    a = "new text"
    f.write(a)

