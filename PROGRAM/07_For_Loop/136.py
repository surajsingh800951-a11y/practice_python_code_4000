# 136. Find the sum of Armstrong numbers.
n=int(input("Enter a number = "))
sum_total=0
for i in range(1,n+1):
    total=0
    cheak=i
    m=len(str(i))
    for j in range(m):
        digit=cheak %  10
        cheak=cheak // 10
        total+=digit ** m
    if i == total:
        sum_total+=i
print("Sum of Armstrong numbers =",sum_total)