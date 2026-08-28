# 103. Count how many times 0 appears.
n=input("Enter a number = ")
count=0
for i in n:
    if int(i) == 0:
        count+=1
print("Count 0 =",count)
        
