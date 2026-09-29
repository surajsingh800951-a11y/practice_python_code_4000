# 122. Find the index/position of the smallest number in a list.
listt = [10, 50, 30, 80, 40]

smallest = listt[0]
position = 0

for i in range(len(listt)):
    if listt[i] < smallest:
        smallest = listt[i]
        position = i

print("Smallest number =", smallest)
print("Index =", position)