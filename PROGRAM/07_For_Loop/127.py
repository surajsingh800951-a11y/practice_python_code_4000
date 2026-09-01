# 127. Count prime numbers between two numbers.
n_1=int(input("Enter first number = "))
n_2=int(input("Enter second number = "))
total=0
for i in range(n_1,n_2+1):
    count=0
    for j in range(1,i+1):
        if count > 2:
            break
        if i % j == 0:
            count+=1
    if count == 2:
        total+=1
        print(i)
print("Count prime numbers between two numbers =",total)            