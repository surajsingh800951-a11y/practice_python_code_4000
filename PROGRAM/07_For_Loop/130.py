# 130. Count the factors of a number.
n=int(input("Enter a number = "))
count=0
for i in range(1,n+1):
    if n % i ==0:
        count+=1
print("Count the factors =",count)