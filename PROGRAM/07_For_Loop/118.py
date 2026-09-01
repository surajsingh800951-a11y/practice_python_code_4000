# 118. Find which digits from 0 to 9 are present.
n = input("Enter a number = ")
for i in range(10):
    if str(i) in n:
        print(i)