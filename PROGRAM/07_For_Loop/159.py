# 159. Print the running sum from 1 to n.
n=int(input("Enter a number = "))
curr=0
prev=0
for i in range(1,n+1):
    curr=prev+i
    prev=curr
    print(curr)
    