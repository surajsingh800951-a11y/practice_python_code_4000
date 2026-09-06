# 144. Check whether two numbers are co-prime.
num1=int(input("Enter first number = "))
num2=int(input("Enter second number = "))
n=min(num1,num2)
hcf_n=0
for i in range(1,n+1):
    if num1 % i ==0 and num2 % i ==0:
        if hcf_n < i:
            hcf_n=i
if hcf_n == 1:
    print("Co-prime")