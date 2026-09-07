# 147. Print only even Fibonacci numbers.
n=int(input("Enter number of terms = "))
a=0
b=1
c=0
for i in range(0,n):
    if c % 2 ==0:
        print(c,end=" ")
        a=b
        b=c
        c=a+b
    else:
        a=b
        b=c
        c=a+b