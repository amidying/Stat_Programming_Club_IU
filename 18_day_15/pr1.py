
with open("poem.txt","r") as f:
    content = f.readlines()
    if "twinkel" in content:
        print("yes present")
    else:
        print("No")
