# 110. Count the number of zeros in a list.
listt = [10, 0, 20, 0, 30, 0, 40]
count=0
for i in listt:
    if i == 0:
        count+=1
print(count)