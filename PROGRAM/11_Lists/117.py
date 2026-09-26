# 117. Find the second-largest number in a list.
listt = [10, 50, 30, 80, 40]
prev=listt[0]
curr=listt[0]
for i in listt:
    if curr < i:
        prev=curr
        curr=i
    elif prev < i and i != curr:
        prev=i
print("Second-largest number in a list =",prev)