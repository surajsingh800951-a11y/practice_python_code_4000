# 138. Count palindrome numbers.
n=int(input("Enter a number = "))
count=0
for i in range(1,n+1):
    rev=0
    m=i
    for j in range(len(str(i))):
        digit=m % 10
        rev=rev*10+digit
        m=m // 10
    if i == rev:
        count+=1
print("Count palindrome numbers =",count)
