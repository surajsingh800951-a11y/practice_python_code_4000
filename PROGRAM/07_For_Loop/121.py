# 121. Count how many times the largest digit appears.
n=int(input("Enter a number = "))
count=0
large=0
digits=[]
for i in range(len(str(n))):
    digit=n % 10
    n=n // 10
    digits.append(digit)
    if large < digit:
        large=digit
for i in range(len(digits)):
    if large == digits[i]:
        count+=1        
print("largest digit",count,"times")