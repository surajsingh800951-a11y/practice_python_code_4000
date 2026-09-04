# 140. Find the sum of all prime numbers from 1 to n.
n=int(input("Enter a number = "))
total_sum=0
for i in range(1,n+1):
    rev=0
    cheak=i
    for j in range(len(str(i))):
        digit=cheak % 10
        cheak=cheak // 10
        rev=rev*10+digit
    if rev == i:
        total_sum+=i
print("Sum of all prime numbers from 1 to n =",total_sum)    