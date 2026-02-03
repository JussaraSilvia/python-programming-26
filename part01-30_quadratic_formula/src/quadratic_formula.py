# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

delta = (b**2) - (4*a*c)
delta1 = sqrt(delta)
x1 = (-b + delta1)/(2*a)
x2 = (-b - delta1)/(2*a)

print("The roots are", x1, " and", x2)