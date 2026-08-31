# 111. Find the difference between the largest and smallest digit.
n=int(input("Enter a number = "))
small=9
large=0
for i in range(len(str(n))):
    digit=n % 10
    n=n // 10
    if large < digit:
        large=digit
    if small > digit:
        small = digit
print("Difference between the largest and smallest digit =",large-small)