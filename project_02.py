# Greeting for Tip Calculator:
print("Welcome to Tip Calculator!")
# Asking amount of Bill:
bill = float(input("What was the total bill? $"))
# Asking amount of Tip in %age:
tip = float(input("How much tip would you want to give? 10, 12 or 15? "))
# Division of Bill in between Person:
person = int(input("How many people split the bill? "))
# Calculating Amount for each Person:
print(f"Each person should pay: ${bill/person+tip/100}")