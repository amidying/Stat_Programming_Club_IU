
# num = int(input("Enter your number: "))
# print(num%5)

run = True
while run:
    num = int(input("Enter your number: "))
    if num==0:
        run = False
    else:
        print(num%5)