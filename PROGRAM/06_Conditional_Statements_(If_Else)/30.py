## 30. Find the second largest among three numbers.
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the three number = "))
if a >= b and a >= c:
    if b >= c:
        print("Second Largest Number =",b)
    else:
        print("Second Largest Number =",c)
elif b >= a and b >= c:
    if a <= c:
        print("Second Largest Number =",c)
    else:
        print("Second Largest Number =",a)
else:
    if a <= b:
        print("Second Largest Number =",b)
    else:
        print("Second Largest Number =",a)
        