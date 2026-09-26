# 114. Reverse a list by manually swapping elements.
listt = [10, 20, 30, 40, 50]
n=len(listt)
for i in range(n // 2):
    temp=listt[i]
    listt[i]=listt[n-1-i]
    listt[n-1-i]=temp
print(listt)