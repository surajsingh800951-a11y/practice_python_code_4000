# 32. Print perfect squares from 1 to n.
n=int(input("Enter a number = "))
for i in range(1,n+1):
    if i*i <= n:
        print(i,"*",i,"=",i*i)