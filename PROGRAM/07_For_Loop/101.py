# 101. Count even digits.

# 1  method

# n=input("Enter a number = ")
# count=0
# for i in n:
#     if int(i) % 2 == 0:
#         count+=1
# print("Count even digit =",count)

#  2 method

n=int(input("Enter a number = "))
count=0
for i in range(len(str(n))):
    if int(i) % 2 == 0:
        count+=1
print("Count even digit =",count)

