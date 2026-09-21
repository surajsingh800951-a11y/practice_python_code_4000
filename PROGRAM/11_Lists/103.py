# 103. Find the largest number in a list without using max().
listt=[10,50,20,80,30]
larg=listt[0]
for i in listt:
    if larg < i:
        larg=i
print(larg)
