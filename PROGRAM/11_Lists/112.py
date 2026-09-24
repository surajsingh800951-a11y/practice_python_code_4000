# 122. Find duplicate values in a list.
# 116. Count the total number of odd numbers in a list.
# 103. Find the largest number in a list without using max().
listt=[10,50,20,80,30]
larg=listt[0]
for i in listt:
    if larg < i:
        larg=i
print(larg)
