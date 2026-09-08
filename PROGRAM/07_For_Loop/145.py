# 145. Print the Fibonacci series.
a=0 # 0 , 1 , 1 , 2 , 3
b=1 # 1 , 1 , 2 , 3 , 5
c=0 # 0 , 1 , 2 , 3 , 5
n=int(input("Enter number of terms = "))
for i in range(0,n):
    print(c,end=" ") 
    a=b 
    b=c 
    c=a+b 
