# 120. Sort a list in descending order without using sort().
listt = [50, 20, 40, 10, 30]

for i in range(len(listt)):
    for j in range(i + 1, len(listt)):
        if listt[i] < listt[j]:
            temp = listt[i]
            listt[i] = listt[j]
            listt[j] = temp

print(listt)