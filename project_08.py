print("<=== Password Strength Checker ===>")
password = input("Enter Your Password: ")

def medium():
    if password.islower() ==1:
        print("Password must include lower case characters.")
    elif password.isupper() ==1:
        print("Password must include upper case characters.")
    elif password.isdigit() ==1:
        print("Password must include digits.")
    elif password.isalnum() ==1:
        print("Password must include special characters..")

def hard():
    if password.islower() >1:
        print("Password must include lower case characters.")
    elif password.isupper() >1:
        print("Password must include upper case characters.")
    elif password.isdigit() >1:
        print("Password must include digits.")
    elif password.isalnum() >1:
        print("Password must include special characters..")

def strong():
    if password.islower() >2:
        print("Password must include lower case characters.")
    elif password.isupper() >2:
        print("Password must include upper case characters.")
    elif password.isdigit() >2:
        print("Password must include digits.")
    elif password.isalnum() >2:
        print("Password must include special characters..")

if len(password) <= 6:
    print("This is a Weak Password. Password must be at least 8 characters.")
elif len(password) >= 8 and len(password) <= 11:
    medium()
    print("This is a medium Password.")
elif len(password) >= 12:
    hard()
    print("This is a hard Password.")
elif len(password) >= 16:
    strong()
    print("This is a strong Password.")