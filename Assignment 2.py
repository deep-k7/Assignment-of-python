# Task 1

num1 = int(input("enter a number: "))

if num1 % 2==0:
    print(f"{num1},is an even number")
else:
    print(f"{num1} is an odd number")

# Task 2

a=0
for i in range(1,51):
    a+=i
print("the sum of number from 1 to 50 is",a)