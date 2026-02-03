# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    sum = number1 + number2
    print(f"{number1} + {number2} = {sum}")
if operation == "multiply":
    mult = number1 * number2
    print(f"{number1} * {number2} = {mult}")
if operation == "subtract":
    sub = number1 - number2
    print(f"{number1} - {number2} = {sub}")