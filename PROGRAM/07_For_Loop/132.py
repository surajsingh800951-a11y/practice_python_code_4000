# 132. Print all perfect numbers from 1 to n.
n=int(input("Enter a number = "))
for i in range(1,n+1):
    total=0
    for j in range(1,i):
        if i % j == 0:
            total+=j
    if i == total:
        print("Perfect number =",i)