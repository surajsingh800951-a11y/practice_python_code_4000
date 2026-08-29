# 109. Find the sum of the first and last digit.
n=int(input("Enter a number = "))
#n=87644
m=n % 10
sum=0
for i in range(len(str(n))):
    digit= n % 10
    n=n // 10
    if n == 0:
        sum +=digit
print("sum of the first and last digit =",sum+m)