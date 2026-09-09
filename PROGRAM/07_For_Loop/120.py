# 120. Print digits in descending order.
n=int(input("Enter a number = "))
digits=[]
for i in range(len(str(n))):
    digit=n % 10
    n=n // 10
    digits.append(digit)
for i in range(len(digits)):
    for j in range(i+1,len(digits)):
        if digits[i] < digits[j]:
            digits[i],digits[j]=digits[j],digits[i]
for i in range(len(digits)):
    print(digits[i],end="")