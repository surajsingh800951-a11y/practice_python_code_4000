# 122. Find the sum of even digits and odd digits separately.
n=int(input("Enter a number = "))
odd_total=0
even_total=0
for i in range(len(str(n))):
    digit= n % 10
    n=n//10
    if digit % 2 ==0:
        even_total+=digit
    else:
        odd_total+=digit
print("Sum of even digits =",even_total)
print("Sum of odd digits =",odd_total)