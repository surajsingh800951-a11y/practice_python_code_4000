# 104. Find the average of digits.
n=(input("Enter a number = "))
count=0
sum=0
for i in n:
    sum+=int(i)
    count+=1
print("Average of digits =",sum/count)    