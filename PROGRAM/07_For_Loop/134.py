# 134. Check whether a number is Armstrong.
n=int(input("Enter a number = "))
cheak=n
total=0
for i in range(len(str(n))):
    digit=n % 10
    n=n // 10
    total+= digit ** 3
if total == cheak:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")