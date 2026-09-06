# 143. Find the LCM of two numbers.
num1=int(input("Enter first number = "))
num2=int(input("Enter second number  = "))
n=max(num1,num2)
lcm_n=n
for i in range(n,num1 * num2 + 1):
    if i % num1 ==0 and i % num2 ==0:
            lcm_n=i
            break
print("LCM =",lcm_n)