# 137. Print all palindrome numbers from 1 to n.
n=int(input("Enter a number = "))
for i in range(1,n+1):
    cheak=i
    rev=0
    for j in range(len(str(i))):
        digit= cheak % 10
        cheak=cheak // 10
        rev=rev*10+digit
    if i == rev:
        print(i)