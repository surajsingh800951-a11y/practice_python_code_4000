# 27. Print multiples of 7 from 1 to n.
n=int(input("Enter a number = "))
for i in range(1,n+1):
    if i % 7 == 0:
        print(i)