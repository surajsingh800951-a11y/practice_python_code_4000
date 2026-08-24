# 39. Take n numbers from the user and find their sum.
n=int(input("How many numbers do you want to enter ? = "))
total=0
for i in range(n):
    num=int(input("Enter a number = "))
    total=total+num
print("Sum =",total)