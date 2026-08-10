# 25. Find the factorial of n.
total=1
n=int(input("Enter a number = "))
for i in range(1,n+1):
    total=total*i
print("factorial of ",n,"=",total)