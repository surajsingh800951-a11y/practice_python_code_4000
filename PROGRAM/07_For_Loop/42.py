# 42. Take n numbers and count zeros.
n=int(input("How many numbers do you want to enter ? = "))
count=0
for i in range(n):
    num=int(input("Enter a number = "))
    if num == 0:
        count+=1
print(count,"Zeros Number")