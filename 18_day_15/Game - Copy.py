import random

comp = random.randint(1,11)

run = True
score = 0

while run:
    print("enter q to quite")
    user = input("enter: ")
    if user == "q":
        print(f"computer choosed: {comp}")
        print(f"your score: {score}")
        run = False

    elif int(user) == comp:
        score += 1
        print("you gussed it right")
        comp = random.randint(1,11)
    elif int(user) < comp:
        print("enter a bigger number: ")
    else:
        print("enter a smaller number")

if __name__ == "__main__":
    pass