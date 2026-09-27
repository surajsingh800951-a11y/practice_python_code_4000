# 132. Find the index/position of the largest number in a list.
# 116. Count the total number of odd numbers in a list.
# 103. Find the largest number in a list without using max().
listt=[10,50,20,80,30]
larg=listt[0]
for i in listt:
    if larg < i:
        larg=i
print(larg)
# 116. Count the total number of odd numbers in a list.
# 103. Find the largest number in a list without using max().
listt=[10,50,20,80,30]
larg=listt[0]
for i in listt:
    if larg < i:
        larg=i
print(larg)
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