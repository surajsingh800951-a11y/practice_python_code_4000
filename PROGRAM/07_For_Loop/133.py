# 133. Find the sum of perfect numbers.
n=int(input("Enter a number ="))
total=0
for i in range(1,n+1):
    cheak=0
    for j in range(1,i):
        if i % j == 0:
            cheak+=j
    if i == cheak:
        total+=i
print("Sum of perfect numbers =",total)