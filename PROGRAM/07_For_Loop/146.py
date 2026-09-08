# 146. Print the first n Fibonacci numbers.
n=int(input("Enter a number = "))
a=0    # 0 , 1 , 1 , 2 , 3
b=1    # 1 , 1 , 2 , 3 , 5
c=0    # 0 , 1 , 2 , 3 , 5
for i in range(0,n):
    print(c,end=" ")
    a=b
    b=c
    c=a+b 