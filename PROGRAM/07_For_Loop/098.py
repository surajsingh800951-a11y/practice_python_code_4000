# 98. Find the largest digit.
n=int(input("Enter a number = "))
# n=987
larg=0
for i in range(len(str(n))):
    digit=n % 10
    n=n//10
    if larg < digit:
        larg = digit
        
print("Largest digit = ",larg)