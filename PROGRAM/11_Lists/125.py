# 125. Write a program to create a nested list representing student records organized in groups.
# 118. Find the second-smallest number in a list.
listt = [10, 50, 30, 80, 40]
prev=listt[0]
curr=listt[0]
for i in listt:
    if curr > i:
        prev=curr
        curr=i
    elif prev > i and i != curr:
        prev=i
print("Second-smallest number in a list =",prev)