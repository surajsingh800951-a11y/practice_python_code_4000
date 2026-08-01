## 110. Check whether a number is divisible by both 2 and 7.
num=int(input("Enter the number = "))
if num % 2 == 0 and num % 7 == 0:
    print("This number is divisible by both 2 and 7 =",num)
else:
    print("This number is not divisible by both 2 and 7 =",num)
