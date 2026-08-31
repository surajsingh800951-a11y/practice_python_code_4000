# 114. Count distinct digits.
n=input("Enter a number = ")
count=0
done=""
for i in n:
    if i not in done:
        count+=1
        done+=i 
print("Count of distinct digits =", count)
