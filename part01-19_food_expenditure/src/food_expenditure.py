# Write your solution here
week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))

cafeteria = week * lunch
cafeteria1 = cafeteria / 7
groceries = money / 7
daily = cafeteria1 + groceries
weekly = cafeteria + money

print("Average food expenditure: ")
print("Daily: ", daily, " euros")
print("Weekly: ", weekly, " euros")