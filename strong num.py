import math

num = int(input("Enter a number: "))
sum_val = sum(math.factorial(int(d)) for d in str(num))

if num == sum_val:
    print(num, "is a Strong number")
else:
    print(num, "is Not a Strong number")
