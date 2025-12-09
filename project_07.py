print("<=== Simple Calculator ===>")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
print("7. Exit Program")

number_1 = int(input("Enter First Number: "))
number_2 = int(input("Enter Second Number: "))

def addition():
    sum = number_1 + number_2
    print(f"The sum of {number_1} and {number_2} is {sum}. ")

def subtract():
    diff = number_1 - number_2
    print(f"The difference of {number_1} and {number_2} is {diff}. ")

def multiply():
    product = number_1 * number_2
    print(f"The product of {number_1} and {number_2} is {product}. ")

def division():
    div = number_1 / number_2
    print(f"The division of {number_1} and {number_2} is {div}. ")

def modulus():
    mod = number_1 % number_2
    print(f"The modulus of {number_1} and {number_2} is {mod}. ")

def power():
    pow = number_1**number_2
    print(f"The power of {number_1}^{number_2} is {pow}. ")
while True:
    choice = int(input("Enter Your Choice (1-7): "))
    if choice == 1:
        addition()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        division()
    elif choice == 5:
        modulus()
    elif choice == 6:
        power()
    elif choice == 7:
        print("The Program is Exiting.")
        break
    else:
        print("Invalid Input!")