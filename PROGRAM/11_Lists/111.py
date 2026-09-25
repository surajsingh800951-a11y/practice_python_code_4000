# 111. Count the occurrence of a given number without using count().
listt = [10, 20, 10, 30, 10, 40]
n = 10
n = int(input("Enter number: "))
count=0
for i in listt:
    if i == n:
        count+=1
print(count)