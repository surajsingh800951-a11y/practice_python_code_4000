## 34. Remove duplicate elements from a list.
listt1=[1,34,23,65,67,34,1,34,65,23,45,98,23]
listt2=[]
for i in listt1:
    if i not in listt2:
        listt2.append(i)
print(listt2)
    