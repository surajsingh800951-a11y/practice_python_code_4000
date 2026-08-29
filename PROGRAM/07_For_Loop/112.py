# 112. Find the second-largest digit.
# n=input("Enter a number = ")
n=98647
curr=-1
prev=-1
for i in str(n):
    i =int(i)
    if curr < i :
        prev=curr
        curr=i
    elif prev < i and i != curr:
        prev=i
print("second-largest digit =",prev)
