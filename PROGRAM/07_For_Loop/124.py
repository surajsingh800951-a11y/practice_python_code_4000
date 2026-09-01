# 124. Check whether a number is prime.
n=int(input("Enter a number = "))
count=0
for i in range(1,n+1):
    if count > 3:
        break
    if n % i == 0 :
        count+=1
if count == 2:
    print("Number is prime")
else:
    print("Number is not prime")
       