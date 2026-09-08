# 148. Find the sum of the series 1 + 2 + 3 + ... + n.
n=int(input("Enter number of terms = "))
total=0
for i in range(1,n+1):
    total+=i
print("Sum of the series 1 + 2 + 3 + ... +",n,"=",total)