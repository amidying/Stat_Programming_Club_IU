num = int(input())

flag = True

if num <2:
    print("Non prime")
else:   
    for i in range(2,num):
        if num == 2:
            break
        if num % i == 0:
            flag = False
            break
    
    if flag:
        print("Prime")
    else:
        print("Non prime")

# cph