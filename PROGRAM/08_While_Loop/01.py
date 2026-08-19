# 1. Keep taking numbers until the user enters 0, then print the sum.
total=0
while True:
    num=int(input("Enter a number = "))
    if num == 0:
        break
    total+=num
print("Sum =",total)