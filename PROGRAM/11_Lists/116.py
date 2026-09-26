# 116. Combine two lists without using the + operator.
list1 = [10, 20, 30]
list2 = [40, 50, 60]
for i in list2:
    list1.append(i)
print(list1)