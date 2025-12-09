import random
choice = int(input("What will you choose? 0 for Rock, 1 for Paper and 2 for Scissor! "))
print(f"Your Choice is: {choice}")
if choice == 0:
    print("Rock")
elif choice == 1:
    print("Paper")
elif choice == 2:
    print("Scissor")
else:
    print("Wrong Choice")

print("Computer's Choice: ")
computers_choice = random.randint(0,2)
if computers_choice == 0:
    print("Rock")
elif computers_choice == 1:
    print("Paper")
elif computers_choice == 2:
    print("Scissor")

if choice == 0 & computers_choice == 2:
    print("You Win!")
elif choice == 1 & computers_choice == 0:
    print("You Win!")
elif choice == 2 & computers_choice == 1:
    print("You Win!")
elif choice == computers_choice:
    print("Its a Draw!")
else:
    print("You Lose!")