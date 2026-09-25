# 109. Separate positive and negative numbers into two different lists.
listt=[10, -5, 20, -15, 0, 30, -8]
positive=[]
negative=[]
for i in range(0,len(listt)):
    if listt[i] < 0:
        negative.append(listt[i])
    else:
        positive.append(listt[i])