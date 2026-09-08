# 149. Find the sum of the odd-number series.
n=int(input("Enter number of terms = "))
total=0
for i in range(1,n+1):
    if i % 2 !=0:
       total+=i 
print("Sum of the odd-number series 1 + 3 + 5 + 7 + ..... + n =",total)