num = int(input("Enter a number: "))
sum_val = sum(int(digit) ** len(str(num)) for digit in str(num))

if num == sum_val:
    print(num, "is an Armstrong number")
else:
    print(num, "is Not an Armstrong number")
