# 113. Reverse a list without using reverse() or [::-1].
listt = [10, 20, 30, 40, 50]
listt2=[]
for i in  range(len(listt)-1,-1,-1):
    listt2.append(listt[i])
print(listt2)