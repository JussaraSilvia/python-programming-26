# Write your solution here
number = float(input("Please type in a number: "))

if number > 0.0:
    integer = int(number)
    decimal = float(number - integer)
    
print("Integer part:", integer)
print("Decimal part:", decimal)