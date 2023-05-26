
# num = 0
i = 0
while i<10:
    try:
        num = int(input("Enter number:"))
        print(num)
    except:
        print("Value Error")
    i +=1