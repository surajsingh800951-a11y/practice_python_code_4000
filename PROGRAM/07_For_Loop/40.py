# 40. Take n numbers and count positive numbers.
n=int(input("How many numbers do you want to enter ? = "))
count=0
for i in range(n):
    num=int(input("Enter a number = "))
    if 0 < num:
        count+=1
print(count,"Positive number")