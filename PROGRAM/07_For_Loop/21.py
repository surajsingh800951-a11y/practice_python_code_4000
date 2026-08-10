# 21. Count even numbers between 1 and n.
count=0
n=int(input("Enter a number = "))
for i in range(1,n+1):
    if i % 2 == 0:
        count=count+1
print("Count even numbers between 1 and n =",count)