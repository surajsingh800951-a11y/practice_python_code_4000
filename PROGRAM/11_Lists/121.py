# 121. Find the index/position of the largest number in a list.
listt = [10, 50, 30, 80, 40]

largest = listt[0]
position = 0

for i in range(len(listt)):
    if listt[i] > largest:
        largest = listt[i]
        position = i

print("Largest number =", largest)
print("Index =", position)