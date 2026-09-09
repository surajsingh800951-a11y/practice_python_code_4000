# 160. Print the running product from 1 to n.
n=int(input("Enter a number = "))
curr=1
prev=1
for i in range(1,n+1):
    curr=prev*i
    prev=curr
    print(curr)