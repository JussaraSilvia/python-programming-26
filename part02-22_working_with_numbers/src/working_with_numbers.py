# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    
    count += 1
    sum += number

    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
mean = sum/count
print("... the program asks for numbers")
print("Numbers typed in", count)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", mean)
print("Positive numbers", positives)
print("Negative numbers", negatives)