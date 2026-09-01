# 121. Count how many times the largest digit appears.
n=int(input("Enter a number = "))
m=n
count=0
larg=0
for i in range(len(str(n))):
    digit=n % 10
    n = n // 10
    if digit > larg:
        larg=digit
for j in str(m):
    if j == str(larg):
        count+=1
print(larg,":",count,"times")