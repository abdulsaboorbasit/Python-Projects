import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','-','+']
numbers = ['1','2','3','4','5','6','7','8','9']

print("Welcome to Password Generator!")
print("Create a Complex Password!")
ls_letters = int(input("How Many Letters do you like in your Password?\n"))
ls_symbols = int(input("How Many Symbols do you like in your Password?\n"))
ls_numbers = int(input("How Many Numbers do you like in your Password?\n"))

password = ""
for char in range(0, ls_letters):
    password += random.choice(letters)
for char in range(0, ls_symbols):
    password += random.choice(symbols)
for char in range(0, ls_numbers):
    password += random.choice(numbers)

print(password)