# Write your solution here
hourly = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily = hourly * hours

if day == "Sunday":
    daily *= 2

print("Daily wages:", daily, "euros")