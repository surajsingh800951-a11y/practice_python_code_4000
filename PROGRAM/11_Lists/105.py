# 105. Count the total number of even numbers in a list.
listt = [10, 15, 20, 25, 30, 33]
count=0
for i in listt:
    if i % 2 ==0:
        count+=1
print(count)
