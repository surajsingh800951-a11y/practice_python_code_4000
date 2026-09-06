# 142. Find the HCF/GCD of two numbers.
num1=int(input("Enter first number = "))
num2=int(input("Enter second number = "))
n=min(num1,num2)
hcf_n=0
for i in range(1,n+1):
    if num1 % i==0 and num2 % i ==0:
        #hcf_n=max(hcf_n,i) # max function
        if i > hcf_n:
            hcf_n=i
print("HCF =",hcf_n)          