print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip percentage do you want to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
print(f'Each person should pay: $ {total_bill/people}')