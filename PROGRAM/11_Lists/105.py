# 105. Count the total number of even numbers in a list.
# 104. Find the smallest number in a list without using min().
listt=[10,50,5,80,30]
smal=listt[0]
for i in listt:
    if smal > i:
        smal=i
print(smal)
