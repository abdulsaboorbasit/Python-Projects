# Treasure Island Game
print("Welcome to Treasure Island!")
choice_1 = input("Your mission is to find the treasure. What will you choose left or right? ")
if choice_1.lower() == "left":
    choice_2 = input("What will you do? Swim or wait? ")
    if choice_2.lower() == "wait":
        choice_3 = input("Which door will you choose? Red, Yellow or Blue? ")
        if choice_3.lower() == "red":
            print("Burned by fire. Game Over.")
        elif choice_3.lower() == "yellow":
            print("You Win!")
        elif choice_3.lower() == "Blue":
            print("Eaten by beats. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")