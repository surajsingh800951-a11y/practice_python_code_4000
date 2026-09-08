# 150. Find the sum of the even-number series.
n=int(input("Enter number of terms = "))
total=0
for i in range(1,n+1):
    if i % 2 ==0:
        total+=i
print("Sum of the even-number series 2 + 4 + 6 + 8 + ..... + n =",total)