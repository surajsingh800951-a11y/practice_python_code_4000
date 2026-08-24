# 46. Take 10 numbers and find the second-smallest number.
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
if a < b:
    curr=a
    prev=b
else:
    curr=b
    prev=a
for i in range(8):
    num=int(input("Enter a number = "))
    if num < curr:
        prev=curr
        curr=num
    elif num < prev:
        prev=num
print("Second smallest number =",prev)