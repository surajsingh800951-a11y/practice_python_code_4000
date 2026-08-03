## 106. Find the largest of three numbers.
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if a < b :
    if b < c:
        print("Largest number =",c)
    else:
        print("Largest number =",b)
elif a < c:
    print("Largest number =",c)
else:
    print("Largest number =",a)
    