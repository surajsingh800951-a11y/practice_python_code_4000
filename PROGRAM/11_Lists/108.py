# 108. Create a new list containing only odd numbers.
listt = [10, 15, 20, 25, 30, 33]
listt2=[]
for i in range(0,len(listt)):
    if listt[i] % 2 != 0:
        listt2.append(listt[i])
print(listt2)
