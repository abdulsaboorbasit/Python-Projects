print('''          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________''')

print("Welcome To The Treasure Island")
print("Your Mission is to find the treasure.")
print("You are on a cross road. Where do you want to go?")
choice_1 = input('\tType "Right" or "Left"\n').lower()
if choice_1 == "left":
    choice_2 = input("You've come to a lake. There is an island in middle of lake."
                     "\n Type 'Wait' to wait for a boat.\n Type 'Swim' to swim across.\n").lower()
    if choice_2 == "wait":
        choice_3 = input("You've arrived on the island unharmed.\n"
                         "There is a house with 3 doors. One red,\n"
                         "one yellow, one blue. What will you choose?\n").lower()
        if choice_3 == "red":
            print("An angry solider comes and kill you.")
        elif choice_3 == "yellow":
            print("You Win!")
        else:
            print("An angry solider comes and kill you.")
    else:
        print("A crocodile comes in lake and kill you.")
else:
    print("You fall in a big hole.")