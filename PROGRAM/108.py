## 108. Check whether a number is a two-digit number.
num=int(input("Enter the number = "))  # only  Positive number
if num >= 10 and num <= 99:    # if 10 <= num <= 99: Same logic
    print("This number is two digit = ",num) 
else:
    print("This number is not two digit = ",num)