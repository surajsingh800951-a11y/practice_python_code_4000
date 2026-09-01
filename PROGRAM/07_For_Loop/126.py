# 126. Print all prime numbers between two numbers.
num_1=int(input("Enter first number = "))
num_2=int(input("Enter second number = "))
for i in range(num_1,num_2+1):
    count=0
    for j in range(1,i+1):
        if count > 3:
            break
        if i % j == 0:
            count+=1
    if count == 2:
        print("Prime number :",i)
  