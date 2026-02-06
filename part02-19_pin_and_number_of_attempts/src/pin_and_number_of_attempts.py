# Write your solution here
pin_correct = "4321"
attempts = 0

while True:
    pin = input("PIN: ")
    attempts += 1

    if pin != "4321":
        print("Wrong")
    elif pin == "4321" and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin == "4321" and attempts > 1:
        print("Correct! It took you", attempts," attempts")
        break