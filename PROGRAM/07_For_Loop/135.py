# 135. Print all Armstrong numbers from 1 to n.
n=int(input("Enter a number = "))
for i in range(1,n+1):
    total=0
    cheak=i
    m=len(str(i))
    for j in range(m):
        digit=cheak % 10
        cheak = cheak // 10
        total+=digit ** m
    if total == i:
        print(i)
        