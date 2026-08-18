# 43. Take n numbers and find the sum of even numbers.
n=int(input("How many numbers do you want to enter ? = "))
total=0
for i in range(n):
    num=int(input("Enter a number = "))
    if num % 2 == 0:
        total+=num
print("Sum of even numbers =",total)