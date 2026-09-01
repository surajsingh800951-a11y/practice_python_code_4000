# 129. Find the sum of factors.
n=int(input("Enter a number = "))
total=0
for i in range(1,n+1):
    if n % i == 0:
        total+=i
print("Sum of factors =",total)