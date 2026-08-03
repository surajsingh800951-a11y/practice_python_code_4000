## 107. Find the smallest of three numbers.
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if a < b:
    if a < c:
        print("Smallest number =",a)
    else:
        print("Smallest number =",c)
elif b < c :
    print("Smallest number =",b)
else:
    print("Smallest number =",c)