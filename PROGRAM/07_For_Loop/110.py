# 110. Find the product of the first and last digit.
n=int(input("Enter a number = "))
last=n % 10
for i in range(len(str(n))):
    digit= n % 10
    n = n // 10
    if n == 0:
        first=digit
print("Product of first and last digit =",first*last)