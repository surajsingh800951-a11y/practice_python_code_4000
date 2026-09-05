# 140. Find the sum of all prime numbers from 1 to n.
n=int(input("Enter a number = "))
total_sum=0
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i % j ==0:
            count+=1
    if count == 2:
        total_sum+=i
print("Sum of all prime numbers from 1 to n =",total_sum)    