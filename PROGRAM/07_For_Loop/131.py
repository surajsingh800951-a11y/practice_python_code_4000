# 131. Check whether a number is perfect.
n=int(input("Enter a number = "))
fact_sum=0
for i in range(1,n):
    if n % i == 0:
        fact_sum+=i
if fact_sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")