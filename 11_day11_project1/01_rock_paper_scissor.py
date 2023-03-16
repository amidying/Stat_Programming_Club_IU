import random

option = ['r','p','s']

comp = random.choice(option)

my_choice = input("Enter your choice: ").lower()
# my_choice = my_choice.lower()

if my_choice == comp:
    print("Draw")
elif my_choice == 'r' and comp == 's':
    print("You win")
elif my_choice == 's' and comp == 'p':
    print("You win")
elif my_choice == 'p' and comp == 'r':
    print("You win")
else:
    print("You lose.")

print(f"You choose: {my_choice} and computer choosed: {comp}")