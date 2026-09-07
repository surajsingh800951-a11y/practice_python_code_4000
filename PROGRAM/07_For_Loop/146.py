# 146. Print the first n Fibonacci numbers.
n=int(input("Enter a number = "))
a=0
b=1
c=0
for i in range(0,n):
    print(c,end=" ")
    a=b
    b=c
    c=a+b