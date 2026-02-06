# Write your solution here
year = int(input("Please type in a year: "))
next_leap = year + 1

while True:
    if next_leap % 100 == 0:
        if next_leap % 400 == 0:
            leap = True
        else:
            leap = False
    elif next_leap % 4 == 0:
        leap = True
    else:
        leap = False

    if leap == True:
        print(f"The next leap year after {year} is {next_leap}")
        break
    else:
        next_leap += 1