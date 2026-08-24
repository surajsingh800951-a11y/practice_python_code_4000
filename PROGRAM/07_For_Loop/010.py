# 10. Find the product of numbers from 1 to n.
total=1
n=int(input("Enter a number = "))
for i in range(1,n+1):
    total=total*i
print("Product ( 1 -- ",n," ) =",total)