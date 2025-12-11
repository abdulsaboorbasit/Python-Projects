import random
print("<=== Welcome to Number Guess Game! ===>")
attempts = 0

while True:
    print("1. Start")
    print("2. Exit")
    choice = int(input("Enter Your Choice (1-2): "))
    if choice == 1:
        user_number = int(input("Enter Your Number (1-100): "))
        computer_number = random.randint(1,100)
        print(f"User Number = {user_number}")
        print(f"Computer's Number = {computer_number}")
        attempts += 1
        if user_number > computer_number:
            print("Your Number is too high.")
        elif computer_number > user_number:
            print("Your Number is too low.")
        elif computer_number == user_number:
            print("Your number is equal to computer's number.")
    elif choice == 2:
        print("The Program is Exiting...")
        break
    else:
        print("Invalid Input!")

print(f"Total Attempts = {attempts}")