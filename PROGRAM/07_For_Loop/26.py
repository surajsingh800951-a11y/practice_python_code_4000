# 26. Find the average of numbers from 1 to n.
total=0
n=int(input("Enter a number = "))
for i in range(1,n+1):
    total+=i # total=total+i
average=total/n
print("Average =",average)