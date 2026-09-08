# 152. Find the sum 1³ + 2³ + 3³ + ... + n³.
n=int(input("Enter number of terms = "))
total=0
for i in range(1,n+1):
    total+=i ** 3
print("Sum 1³ + 2³ + 3³ + ... + n³ =",total)
