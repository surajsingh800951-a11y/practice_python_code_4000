# 23. Find the sum of even numbers from 1 to n.
total=0
n=int(input("Enter a number = "))
for i in range(1,n+1):
    if i % 2 == 0:
        total=total+i
print("Sum of even numbers from 1 to n =",total)