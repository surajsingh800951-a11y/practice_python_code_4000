# 123. Rotate a list to the left by k positions.
listt = [10, 20, 30, 40, 50]
k = 2

for i in range(k):
    temp = listt[0]

    for j in range(len(listt) - 1):
        listt[j] = listt[j + 1]

    listt[-1] = temp

print(listt)