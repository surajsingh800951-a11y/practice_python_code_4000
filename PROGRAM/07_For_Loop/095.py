# 95. Find the product of digits.
n=input("Enter a number = ")
total=1
for i in n:
    total*=int(i)
print("Product of digit =",total)