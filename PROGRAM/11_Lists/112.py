# 112. Find duplicate values in a list.
listt = [10, 20, 30, 20, 40, 10, 50]
listt2=[]
for i in listt:
    count=0
    for j in listt:
        if i == j and i not in listt2:
            count+=1
    if count > 1:
        listt2.append(i)
print(listt2)