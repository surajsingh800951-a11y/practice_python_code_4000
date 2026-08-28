# 102. Count odd digits.
n=input("Enter a number = ")
count=0
for i in n:
    if int(i) % 2 != 0:
        count+=1
print("Count odd digit =",count)