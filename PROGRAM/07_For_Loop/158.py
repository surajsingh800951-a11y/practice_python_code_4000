# 158. Find the sum of factorial values from 1 to n.
n=int(input("Enter a number = "))
total_sum=0
for i in range(1,n+1):
    m=1
    for j in range(i,0,-1):
        m=m*j
    total_sum+=m
print("Sum of factorial values from 1 to n =",total_sum)