# 45. Take 10 numbers and find the second-largest number.
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
if a < b:
    curr=b
    prev=a
else:
    curr=a
    prev=b
for i in range(8):
    num=int(input("Enter a number = "))
    if num > curr:
        prev=curr
        curr=num
    elif num > prev:
        prev=num
print("Second largest number =",prev)