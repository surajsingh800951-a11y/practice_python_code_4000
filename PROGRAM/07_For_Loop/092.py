# 92. Find the least frequent character.
string=input("Enter a string = ")
count=0
min_count=len(string)+1
least=""
for i in string:
    count=0
    for j in string:
        if i == j:
            count+=1
    if count < min_count:
        min_count=count
        least=i
print("Least frequent character =",least)