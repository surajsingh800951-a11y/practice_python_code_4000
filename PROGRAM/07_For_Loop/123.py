# 123. Check whether the first and last digits are the same.
n=int(input("Enter a number = "))
first=0
last=n % 10
for i in range(len(str(n))):
    digit = n % 10
    n=n // 10
    if n == 0:
        first=digit
if first == last:
    print("First and last digits are the same")
else:
     print("First and last digits are not the same")