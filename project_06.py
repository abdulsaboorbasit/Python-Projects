print("Welcome Temperature Unit Converter!")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
temp_value = float(input("Enter Temperature Value: "))
temp_unit = int(input("Enter Temperature Unit: "))

def celsius_fahrenheit():
    temp_fahrenheit = (temp_value * 1.8) + 32
    print(f'The {temp_value} degree Celsius is equal to {temp_fahrenheit} degree Fahrenheit.')

def fahrenheit_celsius():
    temp_celsius = (temp_value - 32) * 5/9
    print(f'The {temp_value} degree Fahrenheit is equal to {temp_celsius} degree Celsius.')

def celsius_kelvin():
    temp_kelvin = temp_value + 273.15
    print(f'The {temp_value} degree Celsius is equal to {temp_kelvin} K.')

def kelvin_celsius():
    temp_celsius = temp_value - 273.15
    print(f'The {temp_value} K is equal to {temp_celsius} degree Celsius.')

if temp_unit == 1:
    fahrenheit_celsius()
elif temp_unit == 2:
    celsius_fahrenheit()
elif temp_unit == 3:
    celsius_kelvin()
elif temp_unit == 4:
    kelvin_celsius()
else:
    print("Invalid Input!")