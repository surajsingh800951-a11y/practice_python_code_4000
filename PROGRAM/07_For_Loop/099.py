# 99. Find the smallest digit.
n=int(input("Enter a number = "))
smal=9
for i in range(len(str(n))):
    digit=n % 10
    if smal > digit:
        smal =digit
    n=n//10
print("Smallest = ",smal)