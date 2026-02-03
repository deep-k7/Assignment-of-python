# task 1
num = int(input("Enter a non-negative integer: "))
factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")

# task 2

import math
n=int(input("Enter a integer: "))
d=math.sqrt(n)
e=math.log(n)
f=math.sin(n)
print(f"The square root of {n} is {d}")
print(f"The square root of {n} is {e}")
print(f"The square root of {n} is {f}")